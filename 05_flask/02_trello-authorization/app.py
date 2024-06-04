from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text, Boolean
from typing import Optional
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

class Base(DeclarativeBase):
    pass

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:trello_dev@localhost:5432/trello'

db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)

'Declare a model'
class Card(db.Model): # Card is arbitrary name
    __tablename__ = 'cards' # Use table name 'cards' to follow the convention.

    id: Mapped[int] = mapped_column(primary_key=True) #Call the mapped_column if there is/are constraints
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(Text) # By default all fields by default is Not Null value. Optional will make the attribute optional.
    date_created: Mapped[date]

class CardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'date_created')

class User(db.Model): # User is arbitrary name
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(200), unique=True)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(200))
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default='false')

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

@app.cli.command('all_cards')
def all_cards():
    stmt = db.select(Card).where(db.or_(Card.id < 3, Card.description != 'Done'))
    print(stmt)
    cards = db.session.scalars(stmt)
    for card in cards:
        print(card.title)

@app.route('/cards')
def all_cards():
    stmt = db.select(Card)
    cards = db.session.scalars(stmt).all()
    return (CardSchema(many=True, only=['id', 'title']).dump(cards))

@app.route('/cards/<int:id>')
def one_card(id):
    card = db.get_or_404(Card, id)
    return CardSchema().dump(card)

@app.route('/users/login', methods=['POST'])
def login():
    # Get the email and password from the request
    # print(type(request.json)) # Flask auto convert json to python dict
    email = request.json['email'] # Extract the data from the request
    password = request.json['password'] # Extract the data from the request
    # [email, password] = request.json # Unpacking the dictionary

    # Compare email and password against db
    stmt = db.select(User).where(User.email == email)
    print(stmt)
    user = db.session.scalar(stmt)
    print(user)
    if user and bcrypt.check_password_hash(user.password, password):
        # Generate the JWT
        # Return the JWT
        return 'Nice one'
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
    return {'error': f'{err}'}
