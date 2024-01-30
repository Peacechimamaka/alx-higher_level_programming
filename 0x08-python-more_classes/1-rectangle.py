#!/usr/bin/python3

'''A module that prints a rectangle
'''


class Rectangle:
    '''A class attribute'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    '''Methods'''

    def width(self):
        return value

    def width(self, value):
        self.value = value
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("height must be >= 0")

    def height(self):
        return value

    def height(self, value):
        self.value == value
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
