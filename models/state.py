#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column("name", String(128), nullable=False)
        cities = relationship("City", back_populates="state", cascade="all,delete")

        def __init__(self, *args, **kwargs):
            super().__init__()
            for k, v in kwargs.items():
                setattr(self, k, v)

            
else:
    class State(BaseModel):
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
