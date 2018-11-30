#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script asks the user how many Fibonnaci numbers to generate and then generates them.
"""


def main():
    num = input("Enter the length of Fibo series")
    for x in range(0, num):
        print fibo(x)


def fibo(n):
    if n == 0 or n == 1:
        return 1

    else:
        return fibo(n-1) + fibo(n-2)


if __name__ == '__main__':
    main()