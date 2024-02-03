#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import String, Column


if getenv("HBNB_TYPE_STORAGE") == "db":
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        __tablename__ = "users"
        email = Column("email", String(128), nullable=False)
        password = Column("password", String(128), nullable=False)
        first_name = Column("first_name", String(128), nullable=False)
        last_name = Column("last_name", String(128), nullable=False)

else:
    class User(BaseModel):
        """This class defines a user by various attributes"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''
