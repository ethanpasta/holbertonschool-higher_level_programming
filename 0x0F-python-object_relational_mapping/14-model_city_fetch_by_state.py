#!/usr/bin/python3
""" Module for task 14 """

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    matches = session.query(City).order_by(City.id).all()
    for city in matches:
        states = session.query(State).filter(State.id == city.state_id).all()
        for state in states:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
