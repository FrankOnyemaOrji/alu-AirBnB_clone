#!/usr/bin/python3
""" Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""


import unittest
import time 
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def setUp(self):
        self.testModel = BaseModel()

    def tearDown(self):
        del self.testModel

    def test_save(self):
        """Testing save method."""
        basemodel = BaseModel()
        updated_at = basemodel.updated_at
        time.sleep(0.5)
        basemodel.save()
        updated_at2 = basemodel.updated_at
        self.assertNotEqual(basemodel.updated_at, basemodel.created_at)
        self.assertNotEqual(updated_at, updated_at2)

    def test_before_save(self):
        """Testing instance attributes before save."""
        self.assertEqual(self.testModel.updated_at, self.testModel.created_at)

    def test_after_save(self):
        """Testing instance attributes after save."""
        self.testModel.save()
        self.assertNotEqual(self.testModel.updated_at, self.testModel.created_at)

    def test_to_dict_return(self):
        """Testing to_dict method."""
        testModelDict = self.testModel.to_dict()
        self.assertEqual(type(testModelDict), dict)

    def test_to_dict_atributes(self):
        """Testing dict attributes."""
        testModelDict = self.testModel.to_dict()
        self.assertIsInstance(testModelDict.get('created_at'), str)
        self.assertIsInstance(testModelDict.get('updated_at'), str)

    def test_to_dict_value(self):
        """Testing dict values."""
        testModelDict = self.testModel.to_dict()
        self.assertIn('__class__', testModelDict)

    def test_str_return(self):
        """Testing __str__ return."""
        class_name = self.testModel.__class__.__name__
        id = self.testModel.id
        dict_value = self.testModel.__dict__
        self.assertEqual(str(self.testModel),
                         f"[{class_name}] ({id}) {dict_value}")
        
if __name__ == "__main__":
    unittest.main()
