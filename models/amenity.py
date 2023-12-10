#!/usr/bin/python3
"""This module defines an Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity.

    Attributes:
        name (str): Name of the instance.
    """
    name = ""
