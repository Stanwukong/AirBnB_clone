#!/usr/bin/python3
"""This module defines a Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place

    Attributes:
        city_id (str): This is the City.id
	user_id (str): This is the User.id
	name (str): Name of the instance
	description (str): Description of the instance. Defaults to empty string
	number_rooms (int): Number of rooms in the instance. Defaults to 0
	number_bathrooms (int): Number of bathrooms in the instance. Defaults to 0
	max_guest (int): Maximum number of guests allowed. Defaults to 0
	price_by_night (int): Price per night. Defaults to 0
	latitude (float): X-coordinates of the place. Defaults to 0.0
	longitude (float): Y-coordinates of the place. Defaults to 0.0
	amenity_ids (list): List of Amenity.id. Empty by default
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
