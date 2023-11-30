#!/usr/bin/python3
""" Module for testing database storage"""
import unittest
from models.engine.db_storage import DBStorage


class test_databaseStorage(unittest.TestCase):
    def test_all(self):
        """ __objects is properly returned """
        storage = DBStorage()
        self.assertIsInstance(storage, DBStorage)