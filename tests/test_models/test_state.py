#!/usr/bin/python3
""" Unittest for State """

import unittest
from models.base_model import BaseModel
from models.state import State


class testState(unittest.TestCase):
    """ Test class for User """

    def test_class(self):
        """ Validate attributes type """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.name, str)
