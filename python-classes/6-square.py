#!/usr/bin/python3
"""Module that defines a Square class with position"""


class Square:
    """Class that defines a square with position and printing"""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with optional size and position
        
        Args:
            size: The size of the square (default: 0)
            position: The position of the square (default: (0, 0))
        """
        self.size = size
        self.position = position
    
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
    
    @property
    def position(self):
        """Getter for position attribute"""
        return self.__position
    
    @position.setter
    def position(self, value):
        """Setter for position attribute with validation"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2
    
    def my_print(self):
        """Print the square with # characters at given position"""
        if self.__size == 0:
            print()
            return
        
        # Print vertical offset (position[1] newlines)
        for i in range(self.__position[1]):
            print()
        
        # Print each row with horizontal offset (position[0] spaces)
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
