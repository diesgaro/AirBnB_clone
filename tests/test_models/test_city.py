#!/usr/bin/python3
"""
test city
"""


import unittest
import os
import pep8
from datetime import datetime as dt
import uuid
from models.city import City
import models.city as ci


class TestCity(unittest.TestCase):
    """
    Test amenity
    """

    def setUp(self):
        """setup function"""
        self.widget = City()

    def test_type_id(self):
        """test id data type"""
        self.assertEqual(type(self.widget.id), str)

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
        new_model = City()
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
        self.assertEqual(class_name, "City")
        self.assertEqual(id, str(self.widget.id))

    def test_access(self):
        """test access"""
        self.assertTrue(os.access('models/city.py', os.R_OK))
        self.assertTrue(os.access('models/city.py', os.W_OK))
        self.assertTrue(os.access('models/city.py', os.X_OK))

    def test_pep8(self):
        """test style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_doc(self):
        """test doc"""
        self.assertTrue(len(ci.__doc__) > 0)
        self.assertTrue(len(City.__doc__) > 0)
