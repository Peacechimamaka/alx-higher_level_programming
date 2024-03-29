#!/usr/bin/python3

''' module for a square class
'''


class Square:
    '''A class that defines a SQUARE
    '''
    def __init__(self, size=0):
        '''An init function'''
        self.__size = size
        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        if size < 0:

            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
