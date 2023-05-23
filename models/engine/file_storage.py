#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ This is a storage engine for AirBnB clone project
    Class Methods:
        all: Returns the object
        new: updates the dictionary id
        save: Serializes, or converts Python objects into JSON strings
        reload: Deserializes, or converts JSON strings into Python objects.
    Class Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
        class_dict (dict): A dictionary of all the classes.
    """
    __file_path = 'storage.json'

    __objects = {}

    def all(self):
        return self.__objects


    def new(self, obj):
        """Add obj with key <obj class name>.id to dictionary.
        Args:
        obj: the object with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        
        self.__objects[key] = obj


    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        json_obj = {}
        for key in self.__objects.keys():
            json_obj[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as json_file:
            json.dump(json_obj, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file"""
        """(path: __file_path) exists ; otherwise, do nothing."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                json_obj = json.load(json_file)
                for key in json_obj.keys():             
                    self.__objects[key] = eval(
                        json_obj[key]['__class__'])(**json_obj[key])
