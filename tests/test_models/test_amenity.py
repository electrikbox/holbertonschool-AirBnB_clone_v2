#!/usr/bin/python3
""" Unittest for Amenity """

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class testAmenity(unittest.TestCase):
    """ Test class for Amenity """

    def test_class(self):
        """ Validate attributes type """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Amenity.name, str)
