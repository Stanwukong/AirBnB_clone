#!/usr/bin/python3
"""This module defines the BaseModel class."""
import models
from datetime import datetime
import uuid


class BaseModel:
    """This represents the class."""

    time = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
        Creates an instance of the BaseModel

        Attributes:
            'id' (str): Unique identifer for each instance.
            'created_at' (datetime): Date and time of creation of the instance.
            'updated_at' (datetime): Current datetime when the object is changed.

        If kwargs is not empty then:
            Each key in kwargs (except '__class__') is treated as an attribute name.
            Each corresponding value is set as the value of the attribute.
            Strings representing 'created_at' and 'updated_at' are converted to datetime objects.

        If kwargs is empty then:
            'id' attribute is set to a unique identifier.
            'created_at' and 'updated_at' attributes are set to the current datetime.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.strptime(value, self.time)
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the class."""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        __class__ returns the class name of the instance.
        self.__dict__ returns instance attributes only.
        Converts created_at and updated_at to ISO format.
        """
        new_dict = self.__dict__.copy()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return (new_dict)
