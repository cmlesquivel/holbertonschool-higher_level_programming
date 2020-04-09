#!/usr/bin/python3
"""Query that get the state that user search
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    get_state = session.query(State).filter(State.name == sys.argv[4]).all()
    if get_state:
        for item in get_state:
            print(item.id)
    else:
        print('Not found')
