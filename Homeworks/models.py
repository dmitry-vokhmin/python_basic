from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    ForeignKey,
)

Base = declarative_base()  # Что делает declarative_base ?


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, autoincrement=True, primary_key=True)
    code = Column(Integer, nullable=False, unique=True)
    name = Column(String, nullable=False)


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    img_link = Column(String)
    category_code = Column(Integer, nullable=False)
    old_price = Column(Float)
    new_price = Column(Float, nullable=False)
    promo_id = Column(Integer, nullable=False)


class Promo(Base):
    __tablename__ = "promo"
    id = Column(Integer, nullable=False, primary_key=True)
    date_begin = Column(String, nullable=False)
    date_end = Column(String, nullable=False)
