#!/usr/bin/python3
"""Defines unnittests for models/amenity.py."""
import os
import unittest
from datetime import datetime

import MySQLdb
import pep8
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker

import models
from models.amenity import Amenity
from models.base_model import Base, BaseModel
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Unittests for testing the Amenity class."""

    @classmethod
    def setUpClass(cls):
        """Amenity testing setup.

        Temporarily renames any existing file.json.
        Resets FileStorage objects dictionary.
        Creates FileStorage, DBStorage and Amenity instances for testing.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.filestorage = FileStorage()
        cls.amenity = Amenity(name="The Andrew Lindburg treatment")

        if type(models.storage) is DBStorage:
            cls.dbstorage = DBStorage()
            Base.metadata.create_all(cls.dbstorage._DBStorage__engine)
            Session = sessionmaker(bind=cls.dbstorage._DBStorage__engine)
            cls.dbstorage._DBStorage__session = Session()

    @classmethod
    def tearDownClass(cls):
        """Amenity testing teardown.
        Restore original file.json.
        Delete the FileStorage, DBStorage and Amenity test instances.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.amenity
        del cls.filestorage
        if type(models.storage) is DBStorage:
            cls.dbstorage._DBStorage__session.close()
            del cls.dbstorage

    # def test_pep8(self):
    #     """Test pep8 styling."""
    #     style = pep8.StyleGuide(quiet=True)
    #     p = style.check_files(["models/amenity.py"])
    #     self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes(self):
        """Check for attributes."""
        us = Amenity(email="a", password="a")
        self.assertEqual(str, type(us.id))
        self.assertEqual(datetime, type(us.created_at))
        self.assertEqual(datetime, type(us.updated_at))
        self.assertTrue(hasattr(us, "__tablename__"))
        self.assertTrue(hasattr(us, "name"))
        self.assertTrue(hasattr(us, "place_amenities"))

    def test_is_subclass(self):
        """Check that Amenity is a subclass of BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_init(self):
        """Test initialization."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_two_models_are_unique(self):
        """Test that different Amenity instances are unique."""
        us = Amenity(email="a", password="a")
        self.assertNotEqual(self.amenity.id, us.id)
        self.assertLess(self.amenity.created_at, us.created_at)
        self.assertLess(self.amenity.updated_at, us.updated_at)

    def test_init_args_kwargs(self):
        """Test initialization with args and kwargs."""
        dt = datetime.now()
        st = Amenity("1", id="5", created_at=dt.isoformat())
        self.assertEqual(st.id, "5")
        self.assertEqual(st.created_at, dt)

    def test_str(self):
        """Test __str__ representation."""
        s = self.amenity.__str__()
        self.assertIn("[Amenity] ({})".format(self.amenity.id), s)
        self.assertIn("'id': '{}'".format(self.amenity.id), s)
        self.assertIn("'created_at': {}".format(
            repr(self.amenity.created_at)), s)
        self.assertIn("'updated_at': {}".format(
            repr(self.amenity.updated_at)), s)
        self.assertIn("'name': '{}'".format(self.amenity.name), s)

    @unittest.skipIf(type(models.storage) is DBStorage,
                     "Testing DBStorage")
    def test_save_filestorage(self):
        """Test save method with FileStorage."""
        old = self.amenity.updated_at
        self.amenity.save()
        self.assertLess(old, self.amenity.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("Amenity." + self.amenity.id, f.read())

    def test_to_dict(self):
        """Test to_dict method."""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(dict, type(amenity_dict))
        self.assertEqual(self.amenity.id, amenity_dict["id"])
        self.assertEqual("Amenity", amenity_dict["__class__"])
        self.assertEqual(self.amenity.created_at.isoformat(),
                         amenity_dict["created_at"])
        self.assertEqual(self.amenity.updated_at.isoformat(),
                         amenity_dict["updated_at"])
        self.assertEqual(self.amenity.name, amenity_dict["name"])


if __name__ == "__main__":
    unittest.main()
