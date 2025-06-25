#!/usr/bin/python3
"""This Square class code."""


class Square:
    """In this class we will get and set size."""

    def __init__(self, size=0):
        """Checking and setting the variable - size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """This is the getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """This is the setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This function returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """This function prints the square with # symbols."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
