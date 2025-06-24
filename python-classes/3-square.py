#!/usr/bin/python3

"""This Square class code."""


class Square:
    """In this class we will get size."""

    def __init__(self, size=0):
        """Checking and getting the variable - size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """This is getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """This is setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This function returns area of square."""
        return self.__size ** 2
