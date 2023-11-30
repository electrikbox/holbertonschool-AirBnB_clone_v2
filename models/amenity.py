#!/usr/bin/python3
""" Amenity Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class Amenity(BaseModel, Base):
    """ The Amenity class, name """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        
        # Define the association table for Many-To-Many relationship
        place_amenities = Table(
            'place_amenity',
            Base.metadata,
            Column(
                'place_id',
                String(60),
                ForeignKey('places.id'),
                primary_key=True,
                nullable=False
            ),
            Column(
                'amenity_id',
                String(60),
                ForeignKey('amenities.id'),
                primary_key=True,
                nullable=False
            )
        )

        # Define the Many-To-Many relationship with Place
        places = relationship(
            'Place',
            secondary=place_amenities,
            back_populates='amenities',
            viewonly=False
        )