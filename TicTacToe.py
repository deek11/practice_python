#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used draw tic tac toe game
"""
import CheckTicTacToe


def draw_board(mx):
    draw_line()
    print "| {0} | {1} | {2} |".format(mx[0][0], mx[0][1], mx[0][2])
    draw_line()
    print "| {0} | {1} | {2} |".format(mx[1][0], mx[1][1], mx[1][2])
    draw_line()
    print "| {0} | {1} | {2} |".format(mx[2][0], mx[2][1], mx[2][2])
    draw_line()


def draw_line():
    print " ---" * 3


def print_result(winner):
    print "\n"
    print "-" * 30
    print " " * 10 + "Winner - {0}".format(winner)
    print "-" * 30


def main():
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    draw_board(game)
    winner = 0

    while moves_left(game):
        p, q = [int(x) for x in raw_input("Player 1,enter your coordinates ").split(",")]
        game = mark_matrix(game, p - 1, q - 1, 'x')
        draw_board(game)

        winner = CheckTicTacToe.find_winner(game)
        if winner != 0:
            break

        p, q = [int(x) for x in raw_input("Player 2,enter your coordinates ").split(",")]
        game = mark_matrix(game, p - 1, q - 1, 'o')
        draw_board(game)

        winner = CheckTicTacToe.find_winner(game)

        if winner != 0:
            break

    print "\n"

    print_result(winner)


def moves_left(mx):
    for i in range(0, 3):
        if 0 in mx[i]:
            return True
    return False


def mark_matrix(mx, x, y, symbol):
    if mx[x][y] == 0:
        mx[x][y] = symbol
    return mx


if __name__ == '__main__':
    main()
