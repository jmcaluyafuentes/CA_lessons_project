from typing import Optional, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
from init import db, ma

class User(db.Model): # User is arbitrary name
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(200), unique=True)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(200))
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default='false')

    cards: Mapped[List['Card']] = relationship(back_populates='user')

class UserSchema(ma.Schema): # Marshmallow
    class Meta:
        fields = ('id', 'email', 'name', 'password', 'is_admin')
