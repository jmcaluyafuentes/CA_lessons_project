from typing import Optional
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey
from init import db, ma
from marshmallow import fields


class Card(db.Model):
    __tablename__ = "cards"

    # id = db.Column(db.Integer, primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)

    # title = db.Column(db.String(100))
    title: Mapped[str] = mapped_column(String(100))
    # description = db.Column(db.Text())
    description: Mapped[Optional[str]] = mapped_column(Text())
    # date_created = db.Column(db.Date())
    date_created: Mapped[date]

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='cards')


# Marshmallow schema (NOT a db schema!)
# Used by Marshmallow to serialize and/or validate our SQLAlchemy models
class CardSchema(ma.Schema):
    class Meta:
        user = fields.Nested("UserSchema", exclude="password")

        fields = ("id", "title", "description", "date_created", "user")