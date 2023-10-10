#!/usr/bin/python3
"""Module containing the Student class definition."""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with a first_name, last_name,
        and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student
        instance."""
        json_dict = {}
        attributes = self.__dict__
        for key, value in attributes.items():
            if isinstance(value, (int, str)):
                json_dict[key] = value
        return json_dict
