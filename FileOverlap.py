#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
    One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
"""


def main():
    prime_list = read_file('primenumbers.txt')
    happy_list = read_file('happynumbers.txt')

    common_list = [int(x) for x in prime_list if x in happy_list]

    print common_list


def read_file(filename):
    num_list = []
    with open(filename, 'r') as p_source:
        line = p_source.readline()
        while line:
            num_list.append(int(line))
            line = p_source.readline()

    return num_list


if __name__ == '__main__':
    main()
