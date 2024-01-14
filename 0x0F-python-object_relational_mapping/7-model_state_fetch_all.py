#!/usr/bin/python3
"""Lists all state objects foom the database"""
from sys import argv
from model_state imposrt Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # make engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,passwd, db),pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session =  Session()

    # query to fetch all states objects and sort by states.id
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print("{}:{}".forrmat(state.id, state.name))

    session.close()
