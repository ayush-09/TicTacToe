"""
Created on Sat Aug 29 20:41:45 2020

@author: ayush
"""

d = {'1 3': ' ', '2 3': ' ', '3 3': ' ', '1 2': ' ', '2 2': ' ', '3 2': ' ', '1 1': ' ', '2 1': ' ', '3 1': ' '}


def print_board():
    print('---------\n|', d['1 3'], d['2 3'], d['3 3'], '|')
    print('|', d['1 2'], d['2 2'], d['3 2'], '|')
    print('|', d['1 1'], d['2 1'], d['3 1'], '|\n---------')


def check_win():
    win_states = [(d['1 3'], d['2 3'], d['3 3']), (d['1 2'], d['2 2'], d['3 2']), (d['1 1'], d['2 1'], d['3 1']),
                  (d['1 3'], d['1 2'], d['1 1']), (d['2 3'], d['2 2'], d['2 1']), (d['3 3'], d['3 2'], d['3 1']),
                  (d['1 3'], d['2 2'], d['3 1']), (d['1 1'], d['2 2'], d['3 3'])]
    if ('O', 'O', 'O') in win_states:
        print("O wins")
        exit()
    elif ('X', 'X', 'X') in win_states:
        print("X wins")
        exit()
    elif all(d[x] != ' ' for x in d.keys()):
        print("Draw")
        exit()


while True:
    i = 0
    coordinates = input("Enter the coordinates: ").split()
    if not coordinates[0].isnumeric() or not coordinates[1].isnumeric():
        print("You should enter numbers!")
        continue
    elif coordinates[0] not in {'1', '2', '3'} or coordinates[1] not in {'1', '2', '3'}:
        print("Coordinates should be from 1 to 3!")
        continue
    elif d[' '.join(coordinates)] != ' ':
        print("This cell is occupied! Choose another one!")
        continue
    else:
        if i % 2 == 0:
            d[' '.join(coordinates)] = 'X'
        else:
            d[' '.join(coordinates)] = 'O'
        i += 1
        print_board()
        check_win()
