#!/usr/bin/python3
"""This module defines a class User."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user

    Attributes:
        email (str): Stores email of the user.
        password (str): Stores the password of the user.
        first_name (str): Stores the first name of the user.
        last_name (str): Stores the last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
