"""
TicTacToe game supporting functions.
"""

# Imports:
import random

def display_board(board):
    print(f' {board[1]} | {board[2]} | {board[3]} \n-----------\n {board[4]} | {board[5]} | {board[6]}\
    \n-----------\n {board[7]} | {board[8]} | {board[9]} \n')


def player_input():
    marker = 0

    while marker == 0:
        choice = str(input('Choose whether to be "X" or "O": ')).upper()

        if choice == 'X' or choice == 'O':
            marker += 1
        else:
            print('That choice is not valid.')

    return choice


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    winning_combs = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7])

    for comb in winning_combs:
        if board[comb[0]] == mark and board[comb[1]] == mark and board[comb[2]] == mark:
            return True
        else:
            continue


def choose_first():
    first = random.randint(1, 2)

    print(('\n') + (f'Player {first} goes first.\n'))
    return first


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return ' ' in board


def player_choice(board):
    choice = 0

    while choice == 0:
        try:
            pos = int(input('Please choose your next position: '))

            if pos >= 1 and pos <= 9:
                if space_check(board, pos):
                    choice += pos
                    return choice
                else:
                    print('Oops, that space is already taken.\n')
                    continue

            print('That choice is not valid.\n')
            continue
        except ValueError:
            print('That choice is not valid.\n')
            continue


def replay():
    again = (input('Would you like to go again? Enter "Y" or "N"... ')).lower()

    return again == 'y'