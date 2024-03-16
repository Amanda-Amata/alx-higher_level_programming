#!/usr/bin/python3
""" Start link class to table in database """

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = sessiomaker(bind=engine)
    session = session()
    for instance in session.query(State).order_by(states.id):
        print(instance.id, instance.name, sep=": ")

