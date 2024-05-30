from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text
from typing import Optional
from flask_marshmallow import Marshmallow

class Base(DeclarativeBase):
    pass

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:trello_dev@localhost:5432/trello'

# Using the old version of SQLAlchemy
# db = SQLAlchemy(app)
# print(vars(db))

# Using the new version of SQLAlchemy
db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow(app)

'Declare a model'
class Card(db.Model):
    __tablename__ = 'cards' # Use table name 'cards' to follow the convention.

    # id = db.Column(db.Integer, primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True) #Call the mapped_column if there is/are constraints

    # title = db.Column(db.String(100))
    title: Mapped[str] = mapped_column(String(100))

    # description = db.Column(db.Text())
    description: Mapped[Optional[str]] = mapped_column(Text)

    # date_created = db.Column(db.Date())
    date_created: Mapped[date]

class CardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'date_created')

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

# @app.cli.command('all_cards')
@app.route('/cards')
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

    # stmt = db.select(Card).where(db.or_(Card.id < 3, Card.description != 'Done'))
    
    # id = 2
    # stmt = db.select(Card).where(Card.id == id)
    # stmt = db.select(Card).filter_by(id = id) #Filter can be used if query if not complex
    # stmt = db.select(Card).where(Card.id != id)
    # stmt = db.select(Card).where(Card.description.like('%Implement%')) # Keyword like is for sub filter. % is a wildcard.
    # stmt = db.select(Card).where(Card.description.like('%Implement%')).order_by(Card.title)
    # stmt = db.select(Card).where(Card.description.like('%Implement%')).order_by(Card.title.desc()) # Descending order
    # print(stmt)

    # cards = db.session.scalars(stmt)
    # for card in cards:
    #     print(card.title)

    # foo = 2
    # card = db.get_or_404(Card, foo)
    # print(card)

    # stmt = db.select(Card).where(Card.id < 2)
    # card = db.one_or_404(stmt)
    # print(card)

    stmt = db.select(Card)
    cards = db.session.scalars(stmt).all()
    # for card in cards:
    #     print(vars(card))
    # return json.dumps(cards, default=lambda c: vars(c)) # This code did not work, therefore use Marsmallow
    # print(CardSchema(many=True).dumps(cards))
    # print(type(CardSchema(many=True).dumps(cards)))
    # print(CardSchema(many=True).dump(cards))
    # print(type(CardSchema(many=True).dump(cards)))

    # return (CardSchema(many=True).dump(cards))
    return (CardSchema(many=True, only=['id', 'title']).dump(cards))

@app.route('/cards/<int:id>')
def one_card(id):
    card = db.get_or_404(Card, id)
    return CardSchema().dump(card)

@app.route('/')
def index():
    return 'Hello world'

@app.errorhandler(404)
def not_found(err):
    return {'error': f'{err}'}

# if __name__ == '__main__':
#     app.run(debug=True)
