#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    # print("db_storage is on")
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    # print("json_storage is on")
    storage = FileStorage()

storage.reload()
__all__ = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review", "storage"]
