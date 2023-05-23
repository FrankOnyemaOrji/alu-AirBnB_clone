#!/usr/bin/python3
"""This module creates an Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class for managing amenity objects"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiates an Amenity object"""
        super().__init__(*args, **kwargs)
