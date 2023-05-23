#!/usr/bin/python3
"""Defines unittests for models/place.py.
Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def setUp(self):
        """Sets up testing environment."""
        self.place = Place()

    def test_Place(self):
        """Testing Place functionality."""
        self.assertIsInstance(self.place.__class__, BaseModel)

    def test_city_id_attr(self):
        """Testing city_id attribute."""
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id_attr(self):
        """Testing user_id attribute."""
        self.assertIsInstance(self.place.user_id, str)

    def test_name_attr(self):
        """Testing name attribute."""
        self.assertIsInstance(self.place.name, str)

    def test_description_attr(self):
        """Testing description attribute."""
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms_attr(self):
        """Testing number_rooms attribute."""
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms_attr(self):
        """Testing number_bathrooms attribute."""
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest_attr(self):
        """Testing max_guest attribute."""
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night_attr(self):
        """Testing price_by_night attribute."""
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude_attr(self):
        """Testing latitude attribute."""
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude_attr(self):
        """Testing longitude attribute."""
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids_attr(self):
        """Testing amenity_ids attribute."""
        self.assertIsInstance(self.place.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
