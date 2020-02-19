#!/usr/bin/python3
"""
test file storage
"""


import unittest
import os
import pep8
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
import models.engine.file_storage as fs


class TestFileStorage(unittest.TestCase):
    """
    Test File Storage
    """

    def setUp(self):
        """initialize test main widget"""
        self.widget = FileStorage()

    @classmethod
    def setUpClass(cls):
        """set up"""
        cls.user = User()
        cls.user.first_name = "Deniel"
        cls.user.last_name = "cabrera"
        cls.user.email = "perdo@joaqion.com"
        cls.storage = FileStorage()

    @classmethod
    def tearDown(cls):
        del cls.user

    def tearDown(self):
        """tear down"""
        try:
            os.remove("file.json")
        except:
            pass

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

    def test_doc_strings(self):
        """test doc strings exists"""
        self.assertTrue(len(fs.__doc__) > 0)
        self.assertTrue(len(FileStorage.__doc__) > 0)
        self.assertTrue(len(FileStorage.new.__doc__) > 0)
        self.assertTrue(len(FileStorage.all.__doc__) > 0)
        self.assertTrue(len(FileStorage.reload.__doc__) > 0)

    def test_pep8(self):
        """ test pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_access(self):
        """testing access"""
        self.assertTrue(os.access('models/engine/file_storage.py', os.R_OK))
        self.assertTrue(os.access('models/engine/file_storage.py', os.W_OK))
        self.assertTrue(os.access('models/engine/file_storage.py', os.X_OK))
