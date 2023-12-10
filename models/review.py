#!/usr/bin/python3
"""This module defines a Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """This represents a review.

    Attributes:
        place_id (str): This is the Place id
        user_id (str): This is the User id
	text (str): The review text.
    """
    place_id = ""
    user_id = ""
    text = ""
