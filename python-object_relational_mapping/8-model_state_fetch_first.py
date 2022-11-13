#!/usr/bin/python3
"""aaaa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """aaaa"""
    try:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(argv[1], argv[2], argv[3]),
        )
    except Exception:
        print("Error")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    ses = Session()
    cont = ses.query(State).order_by(State.id).first()
    if cont:
        print(f"{cont.id}: {cont.name}")
    else:
        print("Nothing")
    ses.close()
