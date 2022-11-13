#!/usr/bin/python3
"""Module list state obj"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == '__main__':
    """new connection"""

    master = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')

    Base.metadata.create_all(master)  # creates table
    NewSession = sessionmaker(master) # join
    new = NewSession()

    states = new.query(State).order_by(State.id)
    for eaach in states:
        print(f"{eaach.id}: {eaach.name}")
