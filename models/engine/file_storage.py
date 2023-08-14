#!/usr/bin/python3
"""Storage that serializes instances to JSON file & deserializes JSON
file to instances:
"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """ serializes instances to a JSON & deserializes JSON"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary objects """
        return self.__objects

    def new(self, obj):
        """ sets in objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes objects to JSON file"""
        json_object = {}
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()
            with open(self.__file_path, 'w') as f:
                json.dump(json_object, f)

    def reload(self):
        """Deserializes the Json file to objects if it exists"""
        try:
            with open(type(self).__file_path, encoding='utf-8') as file:
                objdict = json.load(file)
                for obj in objdict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return

"""    def reload(self):
        deserializes JSON file to __objects
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                for key, value in json.load(f).items():
                    attri_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attri_value
"""
