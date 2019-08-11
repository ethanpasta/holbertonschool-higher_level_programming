#!/usr/bin/python3
"""Module for first orm"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """ Custom class for state object """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False,
                primary_key=True, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade="all, delete-orphan")
