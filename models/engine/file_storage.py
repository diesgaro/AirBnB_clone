#!/usr/bin/python3
"""
File storage module
"""


import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    file management class
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self, *args, **kwargs):
        """
        initialization function
        """

    def all(self):
        """
        return all objects
        """
        return self.__objects

    def new(self, obj):
        """
        set in ibjects the obj with the key class_name.id
        """
        self.__objects[type(obj).__name__ + "."+obj.id] = obj

    def reload(self):
        """
        reload function
        """
        if (os.path.exists(self.__file_path)):
            with open(self.__file_path, "r") as jfile:
                objs = json.loads(jfile.read())
                for key in objs:
                    type_obj = key.split(".")[0]
                    newOb = eval(type_obj + "(**objs[key])")
                    self.__objects[type(newOb).__name__+"."+newOb.id] = newOb

    def save(self):
        """
        save object
        """
        with open(self.__file_path, "w") as jfile:
            objs = {}
            for key in self.__objects.keys():
                objs[key] = self.__objects[key].to_dict()
            json.dump(objs, jfile)
