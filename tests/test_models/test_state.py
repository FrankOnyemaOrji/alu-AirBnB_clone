#1/usr/bin/python3
"""Defines unittests for models/user.py.
Unittest classes:
    TestUser_instantiation
    TestUser_save
     TestUser_to_dict
"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def setUp(self):
        """Sets up testing environment."""
        self.state = State()

    def test_State(self):
        """Testing State functionality."""
        self.assertTrue(self.state.__class__, BaseModel)

    def test_name_attr(self):
        """Testing name attribute."""
        self.assertIsInstance(self.state.name, str)


if __name__ == "__main__":
    unittest.main()
