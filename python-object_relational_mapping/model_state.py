#!/usr/bin/python3
"""Module State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class State(Base):
    """New class: State"""

    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=False)
    name = Coumn('name', String(128), nullable=False)
