#!/usr/bin/python3

"""This Square class code"""


class Square:
    """in this class we will get size"""

    def __init__(self, size=0):
        """checking and getting the variable - size"""

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        if size < 0:

            raise ValueError("size must be >= 0")

        else:
            self.__size = size
    def area(self):
        """This a function wchich returns area of square"""

        return self.__size ** 2
