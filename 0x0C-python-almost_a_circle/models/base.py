#!/usr/bin/python3

'''A module that has a claa base
'''


class Base:
    '''A class base
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''the init function
        '''
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
        if id is not None:
            self.id = id
