# Project: Nessie's Revenge (client)
# File: displaymap.py
# Author: Marissa Baden
# Created: May 23, 2016
# Modified: May 23, 2016

import string

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

def print_remaining_monsters(map):
    ''' Prints monsters you have left to deploy '''
    print("You have " + str(len(remaining_monsters)) + " monster(s) to deploy.\n")

    for name, length in remaining_monsters.items():
        print(name.center(12), repr(length).center(3))

if __name__ == "__main__":
    print("This file is for printing map and flee")
