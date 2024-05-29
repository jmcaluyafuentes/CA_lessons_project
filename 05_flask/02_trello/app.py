from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:trello_dev@localhost:5432/trello'

db = SQLAlchemy(app)
# print(vars(db))

'Declare a model'
class Card(db.Model):
    __tablename__ = 'cards' # Use table name 'cards' to follow the convention.

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    date_created = db.Column(db.Date())

@app.cli.command('db_create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

    # card = Card(title='Start the project', description='Stage 1 - Create ERD', date_created=date.today())
    # card2 = Card(title='ORM Queries', description='Stage 2 - Implement CRUD', date_created=date.today()) 
    # card3 = Card(title='Marshmallow', description='Stage 3 - Implement JSONify of models', date_created=date.today())

    cards = [
        Card(title='Start the project', description='Stage 1 - Create ERD', date_created=date.today()),
        Card(title='ORM Queries', description='Stage 2 - Implement CRUD', date_created=date.today()), 
        Card(title='Marsmallow', description='Stage 3 - Implement JSONify of models', date_created=date.today())
    ]

    # db.session.add(card) # This is like the 'add' (stage) in git
    # db.session.add(card2)
    # db.session.add(card3)

    db.session.add_all(cards)

    db.session.commit() # This is like the 'commit' in git

@app.cli.command('all_cards')
def all_cards():
    # The purpose is to make a query using ORM equivalent to the sql command 'select * from cards;'
    # stmt = db.select(Card) # ORM works with the model and not directly to postgres table
    # print(stmt) # Prints the Card model

    # cards = db.session.execute(stmt)
    # print(cards) # Prints the object iterator

    # cards = db.session.execute(stmt).all() # execute is used for advanced commands
    # print(cards) # Prints the object iterator

    # cards = db.session.execute(stmt)
    # print('Option 1')
    # for card in cards:
    #     print(card)

    # cards = db.session.scalars(stmt).all()
    # print('Option 2')
    # print(cards)

    # cards = db.session.scalars(stmt)
    # print('Option 3')
    # for card in cards:
    #     print(card.title)

    # stmt = db.select(Card).limit(1)
    # card = db.session.scalar(stmt)
    # print(card)

    # stmt = db.select(Card).where(Card.id < 3)
    # cards = db.session.scalars(stmt)
    # for card in cards:
    #     print(card.title)

    stmt = db.select(Card).where(db.or_(Card.id < 3, Card.description != 'Done'))
    # print(stmt)
    cards = db.session.scalars(stmt)
    for card in cards:
        print(card.title)

@app.route('/')
def index():
    return 'Hello world'

# if __name__ == '__main__':
#     app.run(debug=True)

