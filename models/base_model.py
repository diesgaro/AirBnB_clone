#!/usr/bin/python3
"""
Base model module
"""


import uuid
import datetime as dt
import models


class BaseModel:
    """
    defines all commo attributes for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        initialize instance attributes
        """
        if (len(kwargs) != 0):
            self.id = kwargs["id"]
            self.created_at = dt.datetime.strptime(kwargs["created_at"],
                                                   "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = dt.datetime.strptime(kwargs["updated_at"],
                                                   "%Y-%m-%dT%H:%M:%S.%f")
            dic = self.__dict__
            for key in kwargs:
                if key != '__class__':
                    if key not in dic:
                        dic[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = dt.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Object string representation
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     str(self.id),
                                     self.__dict__)

    def save(self):
        """
        save instance update datetime
        """
        self.updated_at = dt.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        return formated dict
        """
        dic = {}
        for key in self.__dict__.keys():
            dic[key] = self.__dict__[key]
        dic["id"] = str(self.id)
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return dic
