#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used 
"""


def draw_horizontal(size=3):
    hlist = [' ']
    for i in range(0, size):
        hlist.append(' ---  ')
    print ''.join(hlist)


def draw_vertical(size):
    vlist = ['| ']
    for i in range(0, size):
        vlist.append('    | ')
    print ''.join(vlist)


def main():
    board_size = input("Enter the board size : ")
    for x in range(0, board_size):
        draw_horizontal(board_size)
        draw_vertical(board_size)

    draw_horizontal(board_size)


if __name__ == '__main__':
    main()
