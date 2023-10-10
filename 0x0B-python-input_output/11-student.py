#!/usr/bin/python3
"""Module Student to disk and reload"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        json_dict = {}
        for attribute in attrs:
            if attribute in self.__dict__:
                json_dict[attribute] = self.__dict__[attribute]
        return json_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance based on the
        provided dictionary."""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
