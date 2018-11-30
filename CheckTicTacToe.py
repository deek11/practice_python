#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used to find a winner of Tic Tac Toe from a 3x3 matrix.
"""


def main():
    mx = [['x', 'x', 'x'],
          [0, 'o', 0],
          ['o', 0, 'x']]

    winner = find_winner(mx)
    if winner != 0:
        print "Winner = {0}".format(winner)
    else:
        print "No winner"


def find_winner(mx):
    # Rows
    for i in range(0, 3):
        row = set([mx[i][0], mx[i][1], mx[i][2]])
        if len(row) == 1 and mx[i][0] != 0:
            return mx[i][0]

    # Columns
    for i in range(0, 3):
        column = set([mx[0][i], mx[1][i], mx[2][i]])
        if len(column) == 1 and mx[0][i] != 0:
            return mx[0][i]

    # Diagonals
    diag1 = set([mx[0][0], mx[1][1], mx[2][2]])
    diag2 = set([mx[0][2], mx[1][1], mx[2][2]])
    if (len(diag1) == 1 or len(diag2) == 1) and mx[1][1] != 0:
        return mx[1][1]

    return 0


if __name__ == '__main__':
    main()
