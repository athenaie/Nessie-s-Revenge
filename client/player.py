# Project: Nessie's Revenge (client)
# File: player.py
# Author: Marissa Baden
# Created: May 21, 2016
# Modified: May 23, 2016
from map import Map

class Player:

    def __init__(self):
        self.name = ''
        self.my_map = Map()
        self.opponent_map = Map()
        self.m_to_deploy = list(range(0,5))
        self.m_surviving = list(range(0,5))
