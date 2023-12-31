#!/usr/bin/python3
"""Module to create a rectangle, class, and methods."""


class Rectangle:
    """Class to create Rectangle objects."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize the width and height of the rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """To delete Rectangle."""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    def __str__(self):
        """Print the rectangle."""
        string = ''
        if self.__width == 0 or self.__height == 0:
            return string
        string += ((str(self.print_symbol) * self.__width + '\n') *
                   self.__height)
        return string[:-1]

    def __repr__(self):
        """To return a String of Rectangle Representation."""
        return "{}({}, {})".format(type(self).__name__,
                                   self.width, self.height)

    @property
    def width(self):
        """To get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """To set the width."""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """To get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """To set the height."""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """To return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """To return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """To return the larger rectangle based on area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """To create a square-type object."""
        return cls(size, size)
