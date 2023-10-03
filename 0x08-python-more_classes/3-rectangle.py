#!/usr/bin/python3
"""Module to create a rectangle class and its methods."""


class Rectangle():
    """Class to create Rectangle objects."""

    def __init__(self, width=0, height=0):
        """Initialize the width and height of the rectangle."""
        self.height = height
        self.width = width

    def __str__(self):
        """Return a string representation of the rectangle."""
        string = ''
        if self.__height == 0 or self.__width == 0:
            return string
        string = string + ('#' * self.__width + '\n') * self.__height
        return string[:-1]

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
