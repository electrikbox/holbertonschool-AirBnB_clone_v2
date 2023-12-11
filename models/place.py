#!/usr/bin/python3
"""This module defines a class Place"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
from models.amenity import Amenity
import models

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table(
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

class Place(BaseModel, Base):
    """ A place to stay """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False
        )
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete-orphan"
        )
        amenity_ids = []
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Returns the list of cities associated with this state."""
            reviews_list = []
            for review in models.storage.all(Review).values():
                if self.id == review.place_id:
                    reviews_list.append(review)
            return reviews_list
        
        @property
        def amenities(self):
            """Get/set linked Amenities."""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
