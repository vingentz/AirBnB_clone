#!/usr/bin/python3
""" Unittest User Class"""
import unittest
import models
import os
from models.user import User


class TestUser(unittest.TestCase):
    """ Test for class User"""

    def test_docstring(self):
        """test if docstring exists"""
        msj = "No docstring"
        self.assertIsNotNone(models.user.__doc__, msj)
        msj = "Class does not have docstring"
        self.assertIsNotNone(User.__doc__, msj)

    def test_executable_file(self):
        """test if file has permissions u+x to execute"""
        is_read_true = os.access('models/user.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/user.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/user.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_init_User(self):
        """test if object is type User"""
        my_object = User()
        self.assertIsInstance(my_object, User)

    def test_id(self):
        """test that id is unique"""
        tstId = User()
        tstId1 = User()
        self.assertNotEqual(tstId.id, tstId1.id)

    def test_attributes(self):
        """test attributes for class user"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_str(self):
        """check if the output of str is in the specified format"""
        my_strobject = User()
        _dict = my_strobject.__dict__
        outstring1 = "[User] ({}) {}".format(my_strobject.id, _dict)
        outstring2 = str(my_strobject)
        self.assertEqual(outstring1, outstring2)

    def test_save(self):
        """ check if date update when save """
        my_objectupd = User()
        first_updated = my_objectupd.updated_at
        my_objectupd.save()
        second_updated = my_objectupd.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        """check if to_dict returns dictionary"""
        my_model3 = User()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'User':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
