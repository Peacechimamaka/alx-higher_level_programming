#!/usr/bin/python3
'''contains a class rectangle that inherits from base
'''
from models.base import Base


class Rectangle(Base):

    '''A sub_class module
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''initializing a class module
        '''
        if type(width) is int:
            self.__width = width
        else:
            raise TypeError('width must be an integer')

        if type(height) is int:
            self.__height = height
        else:
            raise TypeError('height must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x
        if y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is int:
            self__width = value
        else:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

    @height.setter
    def height(self, value):
        if type(value) is int:
            self__height = value
        else:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')

    @x.setter
    def x(self, value):
        if type(value) is int:
            self__x = value
        else:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

    @y.setter
    def y(self, value):
        if type(value) is int:
            self__y = value
        else:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
