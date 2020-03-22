def display_board(board):  # display the board
    print('|', end="")
    print(board[1] + board[2] + board[3] + '|')
    print('|', end="")
    print(board[4] + board[5] + board[6] + '|')
    print('|', end="")
    print(board[7] + board[8] + board[9] + '|')


def player_input():  # Asking Player1 to choose X or O
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1,Choose X or O: ').upper()
    player1 = marker

    if player1 == 'X':
        player2 == 'O'
    else:
        player2 = 'X'
    return (player1, player2)


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (
            board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) or (
                   (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or
                   (board[3] == board[5] == board[7] == mark) or (board[1] == board[5] == board[9] == mark))
