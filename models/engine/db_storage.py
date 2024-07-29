#!/usr/bin/python3
"""create a new db storage engine"""
from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
# from models.__init__ import storage


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """initialize a storage"""
        host = getenv("HBNB_MYSQL_HOST")
        user = getenv("HBNB_MYSQL_USER")
        # hbnb_dev_pwd
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
        f"mysql+mysqldb://{user}:{passwd}@{host}/",
        pool_pre_ping=True)
        connection = self.__engine.connect()

        # Create database if it doesn't exist
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS `{db}`"))

        # Close the connection
        connection.close()
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{passwd}@{host}/{db}",
            pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            metadata = MetaData(bind=self.__engine)
            metadata.reflect()
            metadata.drop_all()

    def all(self, cls=None):
        """get all data from storage"""
        # Session = sessionmaker(bind=self.__engine)
        # self.__session = Session()
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }
        self.reload()
        obj_dict = {}
        # print(cls.__class__.__name__)
        if (cls is not None) and (cls in classes.keys()):
            objs = self.__session.query(classes[cls]).all()
            for obj in objs:
                key = cls + "." + obj.id
                obj_dict[key] = obj

        elif (cls is not None) and (cls in classes.values()):
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = cls.__name__ + "." + obj.id
                # print(obj_dict)
                obj_dict[key] = obj
        else:
            for table in classes.values():
                objs = self.__session.query(table).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload data"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(bind=self.__engine)
        sessionFactory = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(sessionFactory)
        self.__session = Session

    def close(self):
        """close session"""
        self.__session.close()
