#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script takes a list and makes a new list that has only the even elements of this list in it using one line of Python.

"""


def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [x for x in a if x % 2 == 0]
    print b


if __name__ == '__main__':
    main()