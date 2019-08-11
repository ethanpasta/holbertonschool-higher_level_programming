#!/usr/bin/python3
""" Module for task 10 """

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    states_dic = {k: v for k, v in zip(
        [state.name for state in states], [state.id for state in states])}
    if sys.argv[4] in states_dic.keys():
        print(states_dic[sys.argv[4]])
    else:
        print("Not found")

    session.close()
