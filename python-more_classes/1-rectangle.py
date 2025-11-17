#!/usr/bin/python3
"""Module that defines a Rectangle class with width and height"""


class Rectangle:
    """Class that defines a rectangle with width and height properties"""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with optional width and height

        Args:
            width: The width of the rectangle (default: 0)
            height: The height of the rectangle (default: 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
