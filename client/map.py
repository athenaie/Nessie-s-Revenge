# Project: Nessie's Revenge (client)
# File: displaymap.py
# Author: Marissa Baden
# Created: May 23, 2016
# Modified: May 23, 2016

import string

class Map:
''' A graphical representation of a map '''

    def __init__(self, type):
        self.type = type
        self.map = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

    def print_map(map):
        ''' Prints a map to standard output'''

        # print labels from 0-9
        print()
        print('      |=======================================|')
        print('      | ', end='')
        for i in range(0,10):
            print(i, end=' | ')
        print('\n||---||=======================================|')

        # print rows A through J
        for row in range(0,10):
            print('||', string.ascii_uppercase[row], end=' || ')
            for cell in map[row]:
                print(cell, end=' | ')
            print('\n||---||---------------------------------------|')
        print()

    if __name__ == "__main__":
        map = Map()
        print_map(map)
