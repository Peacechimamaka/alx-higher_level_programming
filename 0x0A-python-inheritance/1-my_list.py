#!/usr/bin/python3
'''A module
'''


class MyList(list):
    '''class mylist
    '''

    def print_sorted(self):
        '''function that prints a list in sorted order
        '''
        print(sorted(list(self)))
