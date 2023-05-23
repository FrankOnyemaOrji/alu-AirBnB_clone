#!/usr/bin/python3
"""This module creates a User class"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class that manages state objects"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiates a State object"""
        super().__init__(*args, **kwargs)
