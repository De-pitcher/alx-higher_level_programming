#!/usr/bin/python3
"""This is a rectangle class."""


class Rectangle:
    """This is an empty rectangle class."""
    def __init__(self, width=0, height=0):
        """
        Initialize an instance of MyClass with the given value.

        :param width: The initial value for the instance.
        :prama height: The initial value for the instance.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the value of the 'width' property."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of the 'width' property.

        Args:
            value (int): The new value for the 'width' property.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the value of the 'height' property."""
        return self.__height

    @property
    def height(self):
        """Get the value of the 'height' property."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the 'height' property.

        Args:
            value (int): The new value for the 'height' property.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)
