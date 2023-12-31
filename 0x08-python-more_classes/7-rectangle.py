#!/usr/bin/python3
"""class called Rectangle"""


class Rectangle:
    """ Rectangle class

    Attributes:
        number_of_instances (int): number of instances
        print_symbol (any): symbol used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes the instance

        Args:
            width: rectangle width
            height: rectangle height

        """
        self.width = width
        self.height = height

        type(self).number_of_instances += 1

    @property
    def width(self):
        """returns the value of the width

        Returns:
            rectangle width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """defines the width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """returns the value of the height

        Returns:
            rectangle height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        """returns a string that represents the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""

        return "\n".join([str(self.print_symbol) *
                          self.__width for _ in range(self.__height)])

    def __repr__(self):
        """returns a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """deletes an instance of Rectangle """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
