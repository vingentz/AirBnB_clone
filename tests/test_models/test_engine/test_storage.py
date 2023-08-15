#!/usr/bin/python3
"""file storage test"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    ''' FileStorage test'''

    @classmethod
    def setUpClass(cls):
        """Test set"""
        cls.user = User()
        cls.user.first_name = "Gentz"
        cls.user.last_name = "Karis"
        cls.user.email = "sdfas@hotmail.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """at test end,tear it down"""
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        tstobj = storage.all()
        self.assertIsNotNone(tstobj)
        self.assertEqual(type(tstobj), dict)
        self.assertIs(tstobj, storage._FileStorage__objects)

    def test_new(self):
        """test when creating new"""
        storage = FileStorage()
        tstobj = storage.all()
        user = User()
        user.id = 9876
        user.name = "Gentz"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(tstobj[key])

    def test_reload_filestorage(self):
        """reload test"""
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            first = f.readlines()
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            second = f.readlines()
        self.assertEqual(first, second)
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)

    if __name__ == "__main__":
        unittest.main()
