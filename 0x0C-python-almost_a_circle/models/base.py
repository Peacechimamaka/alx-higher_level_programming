#!/usr/bin/python3

'''A module that has a class base
'''


class Base:
    '''A class base
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''the init function
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
