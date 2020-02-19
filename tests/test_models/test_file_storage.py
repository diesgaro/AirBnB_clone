#!/usr/bin/python3
"""
test file storage
"""


import unittest
import models
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test File Storage
    """

    def setUp(self):
        """initialize test main widget"""
        self.widget = models.storage

    def test_create_instance(self):
        """test instance creation"""
        obj = BaseModel()
        self.widget.new(obj)
        al  = self.widget.all()
        print(al)
        self.assertEqual(type(al[0]), BaseModel)
