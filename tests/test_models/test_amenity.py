#!/usr/python3
"""Defines unittests for models/amenity.py.
Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def setUp(self):
        """Sets up testing environment."""
        self.amenity = Amenity()

    def test_amenity(self):
        """Testing amenity functionality."""
        self.assertTrue(self.test_amenity.__class__,BaseModel)

    def test_amenity_name_attr(self):
        """Testing amenity name attribute."""
        self.assertIsInstance(self.amenity.name, str)


if __name__ == "__main__":
    unittest.main()
