#!/usr/bin/python3

"""This Square class code"""


class Square:
    """in this class we will get size"""

    def __init__(self, size=0):
        """checking and getting the variable - size"""

        self.__size = size

        if not isinstance(int, size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
