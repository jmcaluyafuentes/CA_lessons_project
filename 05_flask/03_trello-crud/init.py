# file name is arbitrary
from os import environ # Encapsulates all of the environment variables (eg., from .env)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager # jwt_required is a decorator

class Base(DeclarativeBase):
    pass

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY') # This is required by JWTManager initialization. The Secret Key was transferred to .env
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')

db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app) # Initialize
