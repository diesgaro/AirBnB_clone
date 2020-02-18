#!/usr/bin/python3
"""
Base model unittest module
"""


import unittest
from datetime import datetime as dt
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test base class
    """
    def setUp(self):
        """initialize test main widget"""
        self.widget = BaseModel()

    def test_type_id(self):
        """test id data type"""
        self.assertEqual(type(self.widget.id), uuid.UUID)

    def test_type_created(self):
        """test created data type"""
        self.assertEqual(type(self.widget.created_at), dt)

    def test_id_not_none(self):
        """test created data type"""
        self.assertIsNotNone(self.widget.id)

    def test_created_not_none(self):
        """test created is not none"""
        self.assertIsNotNone(self.widget.created_at)

    def test_updated_not_none(self):
        """test updated is not none"""
        self.assertIsNotNone(self.widget.updated_at)

    def test_type_updated(self):
        """test updated data type"""
        self.assertEqual(type(self.widget.updated_at), dt)

    def test_difer_id(self):
        """test diferent instances diferent ids"""
        new_model = BaseModel()
        self.assertNotEqual(str(self.widget.id), str(new_model.id))

    def test_to_dict_id_is_str(self):
        """test verify if the dict id is a string type"""
        self.assertIsInstance(self.widget.to_dict()["id"], str)

    def test_to_dict_created_at_is_str(self):
        """test verify if the dict created_at is a string type"""
        self.assertIsInstance(self.widget.to_dict()["created_at"], str)

    def test_to_dict_updated_at_is_str(self):
        """test verify if the dict updated_at is a string type"""
        self.assertIsInstance(self.widget.to_dict()["updated_at"], str)

    def test_time_differ(self):
        """test verify if the time in the current date
        is different to the new date """
        current_time = self.widget.updated_at
        self.widget.save()
        self.assertNotEqual(current_time, self.widget.updated_at)

    def test_verify_magic_str_return(self):
        """test the format returned by __str__"""
        representation = str(self.widget).split(" ")
        class_name = representation[0][1:-1]
        id = representation[1][1:-1]
        self.assertEqual(class_name, "BaseModel")
        self.assertEqual(id, str(self.widget.id))
