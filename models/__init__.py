#!/usr/bin/python3

"""__init__ for models package """

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.state import State


storage = FileStorage()
storage.reload()
