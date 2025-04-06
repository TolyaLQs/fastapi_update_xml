# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Site(Base):
    __tablename__ = "sites"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)
    url = Column(String(200), unique=True)
    filename = Column(String(100), unique=True)


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    site_id = Column(Integer, ForeignKey("sites.id"))
    site = relationship("Site")
    parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    parent = relationship("Category", remote_side=[id])


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category")


class Description(Base):
    __tablename__ = "descriptions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(500))
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category")


class TimeMark(Base):
    __tablename__ = "timemarks"
    id = Column(Integer, primary_key=True, index=True)
    day_of_week = Column(Integer)
    hour = Column(Integer)
    minute = Column(Integer)
    site_id = Column(Integer, ForeignKey("sites.id"))
    site = relationship("Site")


