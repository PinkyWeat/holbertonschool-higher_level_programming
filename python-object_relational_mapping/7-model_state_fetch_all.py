#!/usr/bin/python3
"""Module lists all State objs"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    """New Connection"""
    master = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')

    """Creo las tablas"""
    Base.metadata.create_all(master)

    """Relacionar conexion y modelos"""
    Session = sessionmaker(master)
    newSession = Session()

    """Consulto la base de datos"""
    states = newSession.query(State).order_by(State.id)
    for eaach in states:
        print(f"{eaach.id}: {eaach.name}")
