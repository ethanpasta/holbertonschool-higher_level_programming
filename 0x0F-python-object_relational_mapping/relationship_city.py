#!/usr/bin/python3
""" Module for class state """


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ Custom class city """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"),
                      nullable=False)
