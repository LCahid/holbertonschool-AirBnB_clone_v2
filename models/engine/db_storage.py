#!/usr/bin/python3
"""Data base storage of HBNB"""
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}"
            .format(user, password, host, database),
            pool_pre_ping=True,
        )

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Getting all values from db"""
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}"
                .format(type(obj).__name__, obj.id): obj for obj in objs}

    def new(self, obj):
        """Create new row"""
        self.__session.add(obj)

    def save(self):
        """Save changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete row"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload from db"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False,
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close db"""
        self.__session.close()
