#!/usr/bin/python3
""" city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """ city class inheriting from base model """
    state_id = ""
    name = ""
