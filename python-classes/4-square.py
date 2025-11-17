#!/usr/bin/python3
"""Module that defines a Square class with getter and setter"""


class Square:
    """Class that defines a square with property getter/setter"""
    
    def __init__(self, size=0):
        """Initialize a square with optional size
        
        Args:
            size: The size of the square (default: 0)
        """
        self.size = size
    
    @property
    def size(self):
        """Getter for size attribute
        
        Returns:
            The size of the square
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter for size attribute with validation
        
        Args:
            value: The new size value
            
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """Calculate and return the area of the square
        
        Returns:
            The area of the square (size * size)
        """
        return self.__size ** 2
