#!/usr/bin/python3
"""
BaseModel Class
"""
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import uuid
import models
from os import getenv
time = "%Y-%m-%dT%H:%M:%S.%f"


Base = declarative_base()



class BaseModel:

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    """
    Defines BaseModel class/
    Inherits from SQLAlchemy Base class
    """
    def __init__(self, *args, **kwargs):
        """Initialization  of base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.created_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
         

    def save(self):
        """Updates the attribute 'updated_at with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    # def to_dict(self):
    #     """returns a dictionary containing all keys/values of
    #     __dict__ of the instance. This method creates a dictionary
    #     representation with simple object type.
    #     (serialization/deserialization)
    #     """
    #     dictionary = {}
    #     if self.__dict__ is not None:
    #         dictionary.update({'__class__': self.__class__.__name__})
    #     for key, value in self.__dict__.items():
    #         if key == 'created_at':
    #             dictionary.update({key: self.created_at.isoformat()})
    #         elif key == 'updated_at':
    #             dictionary.update({key: self.updated_at.isoformat()})
    #         dictionary.update({key: value})
    #     return dictionary

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance. This method creates a dictionary
        representation with simple object type.
        (serialization/deserialization)
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop("_sa_instance_state", None)
        return my_dict


    def delete(self):
        """Delete instance"""
        models.storage.delete(self)
