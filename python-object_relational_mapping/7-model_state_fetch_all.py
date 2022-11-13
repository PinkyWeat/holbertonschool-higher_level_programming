#!/usr/bin/python3
"""Module"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """new Connection"""
    try:
        engine = create_engine(f'mysql+mysqldb:/ \
        /{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    except Exception:
        print("Error")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    ses = Session()
    for i in ses.query(State).order_by(State.id).all():
        print(f"{i.id}: {i.name}")
    ses.close()