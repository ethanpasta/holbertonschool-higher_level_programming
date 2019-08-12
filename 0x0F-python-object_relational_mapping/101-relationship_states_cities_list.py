#!/usr/bin/python3
""" Module for task 15 """

if __name__ == "__main__":

    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        cities = state.cities
        for city in cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()
