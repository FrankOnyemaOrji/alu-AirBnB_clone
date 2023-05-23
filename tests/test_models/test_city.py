#!/usr/bin/python3
"""Defines unittests for models/city.py.
Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""

import unittest
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def setUp(self):
        """Sets up testing environment."""
        self.test_city = City()

    def test_City(self):
        """Testing city functionality."""
        self.assertIsInstance(self.test_City.state_id, str)

    def test_city_name(self):
        """Testing city name attribute."""
        self.assertIsInstance(self.test_city.name, str)


if __name__ == "__main__":
    unittest.main()
