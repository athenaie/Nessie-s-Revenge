import string

def print_board(board):
    ''' Prints board (list of lists) to standard output'''

    # print top number labels
    print()
    print('      |=======================================|')
    print('      | ', end='')
    for i in range(0,10):
        print(i, end=' | ')
    print('\n||---||=======================================|')

    # print rest of board
    for row in range(0,10):
        print('||', string.ascii_uppercase[row], end=' || ')
        for cell in board[row]:
            print(cell, end=' | ')
        print('\n||---||---------------------------------------|')
    print()

remaining_monsters = {'Nessie':5, 'Ogopogo': 4,
'Inkanyamba':3, 'Lariousauro':3, 'Muyso':2}

def print_remaining_monsters(board):
    print("You have " + str(len(remaining_monsters)) + " monster(s) to deploy.\n")

    for name, length in remaining_monsters.items():
        print(name.center(12), repr(length).center(3))

if __name__ == "__main__":
    import sys
    print_board(board)
