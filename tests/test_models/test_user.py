#!/usr/bin/python3
""" Unittest for User """

import unittest
from models.base_model import BaseModel
from models.user import User


class testUser(unittest.TestCase):
    """ Test class for User """

    def test_class(self):
        """ Validate attributes type """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(User, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(User.email, str)
            self.assertIsInstance(User.password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.last_name, str)
