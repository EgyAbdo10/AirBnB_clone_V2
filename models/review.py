#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base
        # __tablename__ = "reviews"
        # place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        # user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        # text = Column(String(1024), nullable=False)


if getenv("HBNB_TYPE_STORAGE") == "db":
    class Review(BaseModel, Base):
        """ Review class to store review information """
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
        user = relationship("User", back_populates="reviews")
        place = relationship("Place", back_populates="reviews")

else:
    class Review(BaseModel):
        """ Review class to store review information """
        place_id = ""
        user_id = ""
        text = ""

# echo 'create Review place_id="d2758fa1-d9e3-4d25-a413-dde9b54bff60" user_id="7d94271a-0cae-4451-8dfb-404c0fa49393" text="Amazing_place,_huge_kitchen"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 