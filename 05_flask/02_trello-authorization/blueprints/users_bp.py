from datetime import timedelta
from flask import request
from flask_jwt_extended import create_access_token
from init import db, bcrypt
from models.user import User, UserSchema
from flask import Blueprint

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/login', methods=['POST'])
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