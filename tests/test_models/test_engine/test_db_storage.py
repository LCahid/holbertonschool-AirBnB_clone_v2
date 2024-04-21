#!/usr/bin/python3
""" Module for testing DB storage """
from os import getenv
import unittest
from models.base_model import BaseModel
from models import storage

@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "DBStorage")
class TestDBSorage(unittest.TestCase):
    """ Class to test the database storage method """

    def test_all(self):
        """ method to test the all method of dbStorage """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)