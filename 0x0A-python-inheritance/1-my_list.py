#!/bin/usr/python3
'''A module
'''


class MyList(list):
    '''class mylist
    '''

    def print_sorted(self):
        '''function that prints a list in sorted order
    '''
        sorted_list = sorted(self)
        return(sorted_list)
