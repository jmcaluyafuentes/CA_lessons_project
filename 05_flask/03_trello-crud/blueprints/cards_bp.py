from datetime import date
from flask_jwt_extended import jwt_required
from flask import Blueprint, request
from init import db
from models.card import Card, CardSchema
# from auth import admin_only

cards_bp = Blueprint('cards', __name__, url_prefix='/cards')

# Get all cards (R)
@cards_bp.route('/')
# @admin_only
def all_cards(): # This function was refactored by using the decorator function @admin_only
    stmt = db.select(Card)
    cards = db.session.scalars(stmt).all()
    return (CardSchema(many=True, only=['id', 'title']).dump(cards))

# Get one card (R)
@cards_bp.route('/<int:id>')
# @jwt_required()
def one_card(id):
    card = db.get_or_404(Card, id)
    return CardSchema().dump(card)

# Create a new card (C)
@cards_bp.route('/', methods=['POST'])
@jwt_required()
def create_card():
    card_info = CardSchema(only=["title", "description"], unknown='exclude').load(request.json)
    card = Card(
        title=card_info['title'],
        description=card_info.get('description', ''),
        date_created=date.today()
    )
    db.session.add(card)
    db.session.commit()
    return CardSchema().dump(card), 201

# Update an existing card (U)
@cards_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_card(id):
    card = db.get_or_404(Card, id)
    card_info = CardSchema(only=["title", "description"], unknown='exclude').load(request.json)
    card.title = card_info.get('title', card.title)
    card.description = card_info.get('description', card.description)
    db.session.commit()
    return CardSchema().dump(card), 200

# Delete an existing card (D)
@cards_bp.route('/<int:id>', methods=['DELETE'])
# @jwt_required()
def delete_card(id):
    card = db.get_or_404(Card, id)
    db.session.delete(card)
    db.session.commit()
    return {}
