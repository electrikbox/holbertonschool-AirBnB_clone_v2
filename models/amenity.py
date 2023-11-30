#!/usr/bin/python3
""" Amenity Module for HBNB project """

from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class Amenity(BaseModel, Base):
    """ The Amenity class, name """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)        
        place_amenities = relationship(
            'Place',
            secondary=Place.place_amenity,
            back_populates='amenities',
            viewonly=False
        )