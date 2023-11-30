#!/usr/bin/python3
""" Unittest for City """

import unittest
from models.base_model import BaseModel
from models.city import City


class testCity(unittest.TestCase):
    """ Test class for City """

    def test_class(self):
        """ Validate attributes type """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.state_id, str)
