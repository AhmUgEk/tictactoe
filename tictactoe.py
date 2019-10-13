"""
Simple two-player TicTacToe game.
"""

# Imports:
from tictactoe_functions import choose_first, display_board, full_board_check, place_marker, player_choice, player_input, replay, win_check
from time import sleep


board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

demo_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']

while True:
    print('Welcome to Tic Tac Toe!\n')
    print('Positions on the board correspond with following numbers: \n')
    display_board(demo_board)
    print()

    while True:
        player_1 = player_input()

        if player_1 == 'X':
            player_2 = 'O'
        else:
            player_2 = 'X'

        player_turn = [choose_first()]

        sleep(3)

        while player_turn[0] > 0:
            if full_board_check(board):
                print('\n' * 100)
                print(f"Player {player_turn[0]}'s turn!\n")
                display_board(board)

                player_pos = player_choice(board)

                if player_turn[0] == 1:
                    place_marker(board, player_1, player_pos)
                    if win_check(board, player_1):
                        print('\n' * 100)
                        print('Player 1 wins the game!\n')
                        display_board(board)
                        player_turn[0] = 0
                    else:
                        player_turn[0] = 2

                elif player_turn[0] == 2:
                    place_marker(board, player_2, player_pos)
                    if win_check(board, player_2):
                        print('\n' * 100)
                        print('Player 2 wins the game!\n')
                        display_board(board)
                        player_turn[0] = 0
                    else:
                        player_turn[0] = 1

            else:
                print('\n' * 100)
                print('Game Over!\n')
                display_board(board)
                player_turn[0] = 0

        if replay():
            board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            player_turn = [choose_first()]
            print('\n' * 100)
            continue
        else:
            break
        break
    break