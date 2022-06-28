#!/usr/bin/python3
"""Real definition of a Rectangle"""


class Rectangle:
    """initialize"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """private instance attribute; to retrieve"""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """private instance attribute, retrieves"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
