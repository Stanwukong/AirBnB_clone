#!/usr/bin/python3
"""This module defines the state module."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state

    Attributes:
        name (str): Name of the state.
    """
    name = ""
