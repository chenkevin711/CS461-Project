from sqlalchemy import Column, Integer, String, Numeric, Text
from app.db import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Numeric)
    description = Column(Text)
    category = Column(String)
