#!/usr/bin/python3
"""Query that add new state
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

    louisiana = State(name='Louisiana')
    session.add(louisiana)

    our_state = session.query(State).filter_by(name='Louisiana').first()
    print(our_state.id)
