#!/usr/bin/python3
"""
Defines a class BaseModel that defines all common
attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self):
        """Instantiates a new model
        Attributes:
            id (string): id of base model
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Return string representation of object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance. This method creates a dictionary
        representation with simple object type.
        (serialization/deserialization)
        """
        dictionary = {}
        if self.__dict__ is not None:
            dictionary.update({'__class__': self.__class__.__name__})
        for key, value in self.__dict__.items():
            if key == 'created_at':
                dictionary.update({key: self.created_at.isoformat()})
            elif key == 'updated_at':
                dictionary.update({key: self.updated_at.isoformat()})
            dictionary.update({key: value})
        return dictionary
