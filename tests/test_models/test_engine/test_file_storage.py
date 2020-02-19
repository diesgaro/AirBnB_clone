#!/usr/bin/python3
"""
test file storage
"""


import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test File Storage
    """

    def setUp(self):
        """initialize test main widget"""
        self.widget = FileStorage()

    def test_create_instance(self):
        """test instance creation"""
        obj = BaseModel()
        self.widget.new(obj)
        al = self.widget.all()
        for key in al:
            if (type(al[key]) == BaseModel):
                self.assertEqual(type(al[key]), BaseModel)

    def test_all(self):
        """test all"""
        obj = BaseModel()
        self.widget.new(obj)
        al = self.widget.all()
        self.assertEqual(type(al), dict)

    def test_save(self):
        """test save"""
        self.widget.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """test reload method"""
        self.widget.reload()
        al = self.widget.all()
        self.assertEqual(type(al), dict)
