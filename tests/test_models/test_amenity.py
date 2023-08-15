#!/usr/bin/python3
""" Amenity Unittest """


import unittest
import models
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test for class Amenity"""

    def test_docstring(self):
        """test if docstring exists"""
        msj = "No docstring"
        self.assertIsNotNone(models.amenity.__doc__, msj)
        msj = "Class does not have docstring"
        self.assertIsNotNone(Amenity.__doc__, msj)

    def test_executable_file(self):
        """test if file has permissions"""
        is_read_true = os.access('models/amenity.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/amenity.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/amenity.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_init_amenity(self):
        """test if an object is an type amenity"""
        my_object = Amenity()
        self.assertIsInstance(my_object, Amenity)

    def test_id(self):
        """ test that id is unique """
        tstId = Amenity()
        tstId1 = Amenity()
        self.assertNotEqual(tstId.id, tstId1.id)

    def test_str(self):
        """check if the output of str is in the specified format"""
        my_strobject = Amenity()
        _dict = my_strobject.__dict__
        string1 = "[Amenity] ({}) {}".format(my_strobject.id, _dict)
        string2 = str(my_strobject)
        self.assertEqual(string1, string2)

    def test_save(self):
        """ check if date update when save """
        my_objectupd = Amenity()
        first_updated = my_objectupd.updated_at
        my_objectupd.save()
        second_updated = my_objectupd.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        """check if to_dict returns a dictionary"""
        my_model3 = Amenity()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'Amenity':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)

    if __name__ == '__main__':
        unittest.main()
