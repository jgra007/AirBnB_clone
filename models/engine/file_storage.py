#!/usr/bin/python3
"""
Import and define class
"""

import json
from models.base_model import BaseModel

class FileStorage:
    """
    File storage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """ 
        sets in __objects the obj with key 
        <obj class name>.id
        """
        key = "{}{}".format(obj__class__.__name___, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file 
        (path: __file_path)
        """
        

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file 
        (__file_path) exists ; otherwise, do nothing. If the file doesnt exist, 
        no exception should be raised)
        """
        pass
