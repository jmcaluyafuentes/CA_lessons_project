from datetime import date
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text
from init import db, ma

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
