#!/usr/bin/python3
"""import and define class"""
from datetime import datetime
import uuid


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
            self.created_at = self.update_at = datetime.now()
            models.storage.new(self)

        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "_class_":
                    setattr(self, key, value)

    def __str__(self):
        """that prints class name, id, dict"""
        return "{} {} {}".format(str(type(self).__name__), self.id,
                                 str(self.__dict__))
