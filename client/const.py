# Project: Nessie's Revenge (client)
# File: displaymap.py
# Author: Marissa Baden
# Created: May 23, 2016
# Modified: May 23, 2016

from enum import IntEnum

class monster_attributes(IntEnum):
    name = 0
    length = 1
    origin = 2

monster_list = [('Nessie', 5, 'Scottish'),
            ('Ogopogo', 4, 'Canadian'),
            ('Inkanyamba', 3, 'South African'),
            ('Lariousauro', 3, 'Italian'),
            ('Muyso', 2, 'Columbian')]

def print_monsters(monsters, attributes, prefix, postfix, columns):
    ''' Prints a subset of the attributes of a subset of the monsters'''
    for monster in monster_list:
        print(prefix, end='')
        for attribute in attributes:
            if columns:
                print(str(monster[attribute].center(15)), end=' ')
            else:
                print(monster[attribute], end=' ')
        print(postfix, end='')
