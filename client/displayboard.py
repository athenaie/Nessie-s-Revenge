import string

board = [
[' ', ' ', 'M', 'X', 'X', '/', ' ', ' ', ' ', ' '],
[' ', '/', ' ', ' ', '/', ' ', ' ', ' ', '/', ' ']
]

def print_board(board):
    ''' Prints board to standard output '''

    # print top number labels
    print('      |=======================================|')
    print('      | ', end='')
    for i in range(0,10):
        print(i, end=' | ')
    print('\n||---||=======================================|')

    # print rest of board


    for i in range(0,2):
        print('||', string.ascii_uppercase[i], end=' || ')
        for cell in board[i]:
            print(cell, end=' | ')
        print('\n||---||---------------------------------------|')


if __name__ == "__main__":
    import sys
    print_board(board)
