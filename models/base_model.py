#!/usr/bin/python3
from datetime import datetime
import uuid
import models


class BaseModel:
    """Class Basemodel that defines common attrs/methods
    for other class"""

    def __init__(self, *arg, **kwargs):
        """Args:
                id: id of instance
                created at: time of creation
                updated_at: time of creation or modification
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """that prints class name, id, dict"""
        return "[{}] ({}) {}".format(str(type(self).__name__), self.id,
                                     str(self.__dict__))

    def __repr__(self):
        """returns object representation"""
        return "[{}] ({}) {}".format(str(type(self).__name__), self.id,
                                     str(self.__dict__))

    def save(self):
        """updates the updated_at attr w/ current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary representation of __dict__"""
        dct = dict(**self.__dict__)
        dct["__class__"] = str(type(self).__name__)
        dct["created_at"] = self.created_at.isoformat()
        dct["updated_at"] = self.updated_at.isoformat()
        return dct
