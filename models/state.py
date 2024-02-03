#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv



class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column("name", String(128), nullable=False)
        cities = relationship("City", back_populates="state", cascade="all,delete")
    else:
        name = ''
        @property
        def cities(self):
            from models.__init__ import storage
            from models.city import City
            city_objs = storage.all(City)
            cities_in_state = []
            for city in city_objs.values():
                if city.state_id == self.id:
                    cities_in_state.append(city)
            return cities_in_state
