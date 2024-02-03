#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
# from models.state import State
from sqlalchemy.orm import relationship
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = "cities"
        state_id = Column("state_id", String(60),
                        ForeignKey("states.id"), nullable=False)
        name = Column("name", String(128), nullable=False)
        state = relationship("State", back_populates="cities")
else:
    class City(BaseModel):
        name = ""
        state_id = ""
