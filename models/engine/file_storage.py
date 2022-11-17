#!/usr/bin/python3
"""Serializes instances to a JSON file and deserializes
   JSON file to instances
"""
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if obj is not None:
            self.__objects.update(obj)

    def save(self):
        """Serializes __objects to the JSON file
        (path: __file_path)
        """
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects only if 
        the (__file_path) exists;otherwise do nothing
        """
        if __file_path is not None:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        else:
            pass
