#!/usr/bin/python3
"""Python Interpreter"""
import json
import os.path


class Base:
    """new class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """new initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """formats to JSON for sharing data"""
        if list_dictionaries is None:
            return "[]"
        else:
            jeison = json.dumps(list_dictionaries)
        return jeison

    @classmethod
    def save_to_file(cls, list_objs):
        """Json string to file"""
        if list_objs is not None:
            list_objs = [elements.to_dictionary() for elements in list_objs]
        with open("{}.json".format(cls.__name__), "w") \
                as tempFile:
            tempFile.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON string"""
        jeisonlist = []
        if json_string is None or len(json_string) == 0:
            return jeisonlist
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all atributes already set"""
        if cls.__name__ == 'Rectangle':
            newInstance = cls(1, 1)
            newInstance.update(**dictionary)
            return newInstance
        if cls.__name__ == 'Square':
            newInstance = cls(1)
            newInstance.update(**dictionary)
            return newInstance
        else:
            pass

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        instances = []
        fileName = cls.__name__ + ".json"
        if os.path.exists(fileName):
            with open(fileName) as tempFile:
                listIntances = []
                obj = cls.from_json_string(tempFile.read())
                for element in obj:
                    listIntances.append(cls.create(**element))
                return listIntances
        else:
            list
