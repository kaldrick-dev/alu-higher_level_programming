#!/usr/bin/python3
"""Module that defines a Square class with printing capability"""


class Square:
    """Class that defines a square with printing capability"""
    
    def __init__(self, size=0):
        """Initialize a square with optional size
        
        Args:
            size: The size of the square (default: 0)
        """
        self.size = size
    
    @property
    def size(self):
        """Getter for size attribute"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter for size attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2
    
    def my_print(self):
        """Print the square with # characters"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
