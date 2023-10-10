#!/usr/bin/python3
"""Module containing the Student class definition."""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance"""
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
