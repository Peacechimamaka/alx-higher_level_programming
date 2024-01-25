#!/usr/bin/python3
''' A module for a square class'''


class Square:
    '''A class that defines a SQUARE'''
    def __init__(self, size=0):
        self__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
