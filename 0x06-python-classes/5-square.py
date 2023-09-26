#!/usr/bin/python3
"""Define a class named Square"""


class Square:
    """This is a class for a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square. Default is 0.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with '#' characters.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for num in range(0, self.__size):
                print('#' * self.__size)
