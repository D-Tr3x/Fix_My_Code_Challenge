#!/usr/bin/python3
"""Module defines a Square class"""


class Square:
    """ Class representing a square (or rectangle) """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializes width and height attributes """
        self.width = 0
        self.height = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Dictionary representation of Square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
