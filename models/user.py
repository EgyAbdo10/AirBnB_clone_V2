#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


if getenv("HBNB_TYPE_STORAGE") == "db":
    class User(BaseModel, Base): 
        """This class defines a user by various attributes"""
        __tablename__ = "users"
        email = Column("email", String(128), nullable=False)
        password = Column("password", String(128), nullable=False)
        first_name = Column("first_name", String(128), nullable=True)
        last_name = Column("last_name", String(128), nullable=True)
        places = relationship("Place", back_populates="user", cascade="all,delete")
        reviews = relationship("Review", back_populates="user", cascade="all,delete")
        # hbnb_dev_pwd
        def __init__(self, *args, **kwargs):
            super().__init__()
            for k, v in kwargs.items():
                setattr(self, k, v)
else:
    class User(BaseModel):
        """This class defines a user by various attributes"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''

# echo 'create Place city_id="566428db-8e1d-4946-9cfe-c6dd3b7d1815" user_id="7d94271a-0cae-4451-8dfb-404c0fa49393" name="Lovely_place" number_rooms=3 number_bathrooms=1 max_guest=6 price_by_night=120 latitude=37.773972 longitude=-122.431297' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
