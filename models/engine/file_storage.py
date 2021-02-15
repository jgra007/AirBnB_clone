#!/usr/bin/python3
"""
Import and define class
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        (path: __file_path)
        """
        new_dict = {}
        for key, item in FileStorage.__objects.items():
            new_dict[key] = item.to_dict().copy()
        with open(FileStorage.__file_path, mode="w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesnt exist,
        no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, mode="r") as file:
                new_dict = (json.load(file))
                for key, value in new_dict.items():
                    class_name = value.get('__class__')
                    obj = eval(class_name + '(**value)')
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
