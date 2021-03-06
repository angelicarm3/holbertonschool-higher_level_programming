#!/usr/bin/python3
"""Base class"""
import json
import os


class Base:
    """Base class this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Defines Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of an object"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes an object to a text file"""
        list = []
        filename = str(cls.__name__)+".json"

        if list_objs is not None:
            for i in range(len(list_objs)):
                list.append(cls.to_dictionary(list_objs[i]))
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """Return the Python object representation of a JSON string."""
        list = []
        if json_string is None:
            return list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all atributes set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        jlist = []
        filename = str(cls.__name__)+".json"

        if os.path.exists(filename):
            with open(filename, mode="r", encoding="utf-8") as file:
                list = cls.from_json_string(file.read())
                for i in list:
                    jlist.append(cls.create(**i))
            return jlist
        else:
            return jlist

    def reset_nb_instances():
        """Resets number of instances"""
        Base.__nb_objects = 0
