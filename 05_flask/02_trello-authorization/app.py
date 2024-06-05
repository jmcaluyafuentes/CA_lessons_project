from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import date, timedelta
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text, Boolean
from typing import Optional
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity # jwt_required is a decorator
from marshmallow.exceptions import ValidationError

class Base(DeclarativeBase):
    pass

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'Ministry of Silly Walks' # This is required by JWTManager initialization

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:trello_dev@localhost:5432/trello'

db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app) # Initialize

'Declare a model'
class Card(db.Model): # Card is arbitrary name
    __tablename__ = 'cards' # Use table name 'cards' to follow the convention.

    id: Mapped[int] = mapped_column(primary_key=True) #Call the mapped_column if there is/are constraints
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(Text) # By default all fields by default is Not Null value. Optional will make the attribute optional.
    date_created: Mapped[date]

class CardSchema(ma.Schema): # Marshmallow
    class Meta:
        fields = ('id', 'title', 'description', 'date_created')

class User(db.Model): # User is arbitrary name
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(200), unique=True)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(200))
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default='false')

class UserSchema(ma.Schema): # Marshmallow
    class Meta:
        fields = ('id', 'email', 'name', 'password', 'is_admin')

@app.cli.command('db_create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

    users = [ # Start with basic values
        User(
            email='admin@spam.com',
            password=bcrypt.generate_password_hash('spinynorman').decode('utf8'),
            is_admin=True
        ),
        User(
            email='cleese@spam.com',
            name='John Cleese',
            password=bcrypt.generate_password_hash('tisbutascratch').decode('utf8')
        )
    ]

    cards = [
        Card(
            title='Start the project',
            description='Stage 1 - Create ERD',
            date_created=date.today()
        ),
        Card(
            title='ORM Queries',
            description='Stage 2 - Implement CRUD',
            date_created=date.today()
        ),
        Card(title='Marshmallow',
             description='Stage 3 - Implement JSONify of models',
             date_created=date.today()
        )
    ]

    db.session.add_all(users)
    db.session.add_all(cards)

    db.session.commit() # This is like the 'commit' in git
    print('Users and Cards added')

def admin_only(fn):
    @jwt_required() # admin_only requires jwt
    def inner():
        # Ensure the user is an admin
        user_id = get_jwt_identity()
        # Query: Fetch a user based on JWT token subject
        stmt = db.select(User).where(User.id == user_id, User.is_admin)
        # Execute query (scalar)
        user = db.session.scalar(stmt)
        # If (user) return cards else return error
        if user:
            return fn()
        else:
            return {'error': 'You must be an admin to access this resource'}, 403

    return inner

@app.route('/cards')
@admin_only
def all_cards(): # This function was refactored by using the decorator function @admin_only
    stmt = db.select(Card)
    cards = db.session.scalars(stmt).all()
    return (CardSchema(many=True, only=['id', 'title']).dump(cards))

@app.route('/cards/<int:id>')
@jwt_required()
def one_card(id):
    card = db.get_or_404(Card, id)
    return CardSchema().dump(card)

@app.route('/users/login', methods=['POST'])
def login():
    # Get the email and password from the request
    # print(type(request.json)) # Flask auto convert json to python dict
    # email = request.json['email'] # Extract the data from the request
    # password = request.json['password'] # Extract the data from the request
    
    # Validation using Marshmallow
    params = UserSchema(only=['email', 'password']).load(request.json, unknown='exclude') # Load is opposite to dump. It de-serialize a data structure to python object.
    
    # [email, password] = request.json # Unpacking the dictionary

    # Compare email and password against db
    stmt = db.select(User).where(User.email == params["email"])
    print(stmt)
    user = db.session.scalar(stmt)
    print(user)
    if user and bcrypt.check_password_hash(user.password, params["password"]):
        # Generate the JWT
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2)) # Can add additional claims but not the sensitive info that can be exploited
        # Return the JWT
        return {'token': token}
    else:
        return {'error': 'Invalid email or password'}, 401
    # Error handling (user not found, wrong username or password)
    
    # return 'ok'

@app.route('/')
def index():
    return 'Hello world'

@app.errorhandler(405)
@app.errorhandler(404)
def not_found(err):
    return {'error': 'Not Found'}

@app.errorhandler(ValidationError)
def invalid_request(err):
    return {'error': vars(err)['messages']}
