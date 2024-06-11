# blueprint folder is like the controller in MVP architechture.
# bp in cli_bp means blueprint. File name is arbitrary

from datetime import date
from flask import Blueprint
from init import db, bcrypt # app is removed because it is replaced by blueprint
from models.user import User
from models.card import Card

db_commands = Blueprint('db', __name__) # cli_commands is arbitrary. __name__ is the import name which is the name of the module
# We can add here other categories not related to db and add cli commands on it.

# @app.cli.command('db_create')
@db_commands.cli.command('create')
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
        ),
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
        ),
    ]

    db.session.add_all(users)
    db.session.add_all(cards)

    db.session.commit() # This is like the 'commit' in git
    print('Users and Cards added')