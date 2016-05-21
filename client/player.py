from displayboard import print_board
from displayboard import print_remaining_monsters

class Player:
    board_size = 10

    def __init__(self):
        self.name = ''
        self.my_board = [
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        ]


def setup_player(player):
    welcome_message()
    player.name = input("Please enter your name: ")
    print()
    greet_player(player.name)


def welcome_message():
    print("Welcome to Nessie's Revenge!")

def greet_player(name):
    print("Hello " + name + "!")
    print("You and your opponent have each captured an army of Lake Monsters:")
    print("Nessie, the Ogopogo, the Inkanyamba, the Lariousauro, and the Muyso.")
    print("You will each hide your monsters in your section of ocean and take",
          "turns firing until one army has been defeated.\n")
    input("Press enter to continue...")
    print()

def setup_my_board(player):
    print("Here is your section of ocean:")
    print_board(player.my_board)
    print_remaining_monsters(player.my_board)




if __name__ == "__main__":
    player = Player()
    setup_player(player)
    setup_my_board(player)
