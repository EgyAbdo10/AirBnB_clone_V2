#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from os import getenv
import json

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column("id", String(60), primary_key=True, nullable=False)
        created_at = Column("created_at", DateTime, nullable=False)
        updated_at = Column("updated_at", DateTime, nullable=False)
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if ("id" not in kwargs.keys()
        and "created_at" not in kwargs.keys()
        and "updated_at" not in kwargs.keys()):
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            del kwargs['__class__']
            self.created_at = kwargs['created_at']
            self.updated_at = kwargs['updated_at']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = self.__class__.__name__
        if getenv("HBNB_TYPE_STORAGE") == "db":
            del self.__dict__['_sa_instance_state']
            new_dict = str(self.__dict__).replace("\"", "")
            return '[{}] ({}) {}'.format(cls, self.id, new_dict)
        else:
            return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        storage.new(self)
        self.updated_at = datetime.now()
        storage.save()
# echo 'create City state_id="4f2f8ff9-0dc1-4efe-a9f3-d8fd6f4a1b86" name="San_Jose"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary.keys():
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """deletes the  current instance from the storage"""
        from models import storage
        storage.delete(self)
