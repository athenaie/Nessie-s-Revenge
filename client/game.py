# Project: Nessie's Revenge (client)
# File: game.py
# Author: Marissa Baden
# Created: May 23, 2016
# Modified: May 23, 2016
from player import Player
from map import Map.print_map
from const import monster_attributes as a


player = Player()

def setup_player():
    global player
    print("Welcome to Nessie's Revenge!")
    player.name = input("Please enter your name: ")
    print()
    greet_player()

def greet_player():
    global player
    print("Hello " + player.name + "!")
    print("You and your opponent have each captured an army of Lake Monsters:")
    print("You will each hide your monsters in your section of ocean and take",
          "turns firing until one army has been defeated.\n")
    input("Press enter to continue...")
    print()
    print("These are your monsters:")
    print_monsters(list(range(0,5)), [a.origin, a.name], 'The', '\n')
    print("And this is your map:")
    print_map(player.my_map)
    print("You can place your monsters along any row or column, but they must",
        "stay within the map and cannot overlap each other.")
    input("Press enter to begin...")

def populate_my_map():
    global player
    while player.m_to_deploy:
        pass
    #TODO continue here

if __name__ == "__main__":
    global player
    setup_player(player)
    populate_my_map(player)
