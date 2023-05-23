#!/usr/bin/python3
"""Defines unittests for models/user.py.
Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def setUp(self):
        """Sets up testing environment."""
        self.user = User()

    def test_User(self):
        """Testing User functionality."""
        self.assertIsInstance(self.user.__class__, BaseModel)

    def test_email_attr(self):
        """Testing email attribute."""
        self.assertIsInstance(self.user.email, str)

    def test_password_attr(self):
        """Testing password attribute."""
        self.assertIsInstance(self.user.password, str)

    def test_first_name_attr(self):
        """Testing first_name attribute."""
        self.assertIsInstance(self.user.first_name, str)

    def test_last_name_attr(self):
        """Testing last_name attribute."""
        self.assertIsInstance(self.user.last_name, str)


if __name__ == "__main__":
    unittest.main()
