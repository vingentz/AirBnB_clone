#!/usr/bin/python3
""" Unittest State """

import unittest
import models
import os
from models.state import State


class TestState(unittest.TestCase):
    """ Test for class State"""

    def test_docstring(self):
        """test if docstring exists"""
        msj = "No docstring"
        self.assertIsNotNone(models.state.__doc__, msj)
        msj = "Class does not have docstring"
        self.assertIsNotNone(State.__doc__, msj)

    def test_executable_file(self):
        """test if file has permissions"""
        is_read_true = os.access('models/state.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/state.py', os.W_OK)
        self.assertTrue(is_exec_true)
        is_exec_true = os.access('models/state.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_init_State(self):
        """test if an object is an type State"""
        my_object = State()
        self.assertIsInstance(my_object, State)

    def test_id(self):
        """ test that id is unique """
        tstId = State()
        tstId1 = State()
        self.assertNotEqual(tstId.id, tstId1.id)

    def test_str(self):
        """check if the output of str is in the specified format"""
        my_strobject = State()
        _dict = my_strobject.__dict__
        string1 = "[State] ({}) {}".format(my_strobject.id, _dict)
        string2 = str(my_strobject)
        self.assertEqual(string1, string2)

    def test_save(self):
        """ check if date update when save """
        my_objectupd = State()
        first_updated = my_objectupd.updated_at
        my_objectupd.save()
        second_updated = my_objectupd.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        """check if to_dict returns a dictionary"""
        my_model3 = State()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'State':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
