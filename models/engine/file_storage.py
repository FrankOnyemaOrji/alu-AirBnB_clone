#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
import datetime


class FileStorage:

    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as file:
            fuss = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(fuss, file)

    def classes(self):
        """Returns a dictionary of classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        return {"BaseModel": BaseModel, "User": User, "State": State,
                "City": City, "Place": Place, "Review": Review,
                "Amenity": Amenity}

    def reload(self):
        """Reloads the stored objects from the JSON file"""
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r') as file:
            fuss = json.reload(file)
            fuss = {k: self.classes()[v["__class__"]](**v)
                                    for k, v in fuss.items()}
            # TODO: check if this works or should this overwrite or insert
            FileStorage.__objects = fuss

    def attributes(self):
        """returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime,
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str,
            },
            "State": {
                "name": str,
            },
            "City": {
                "state_id": str,
                "name": str,
            },
            "Amenity": {
                "name": str,
            },
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list,
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str,
            },
        }
        return attributes