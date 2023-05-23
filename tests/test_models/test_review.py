#!/usr/bin/python3
"""Defines unittests for models/review.py.
Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def setUp(self):
        """Sets up testing environment."""
        self.review = Review()

    def test_Review(self):
        """Testing Review functionality."""
        self.assertIsInstance(self.review.__class__, BaseModel)

    def test_place_id_attr(self):
        """Testing place_id attribute."""
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id_attr(self):
        """Testing user_id attribute."""
        self.assertIsInstance(self.review.user_id, str)

    def test_text_attr(self):
        """Testing text attribute."""
        self.assertIsInstance(self.review.text, str)


if __name__ == "__main__":
    unittest.main()
