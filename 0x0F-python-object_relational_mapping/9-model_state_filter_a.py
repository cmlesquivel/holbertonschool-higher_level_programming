#!/usr/bin/python3
"""Query that get all states that contain 'a'
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

    list_state_contain_a = session.query(
        State).filter(State.name.contains('a')).order_by(State.id)

    for item in list_state_contain_a:
        print('{}: {}'.format(item.id, item.name))
