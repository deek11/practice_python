#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used to perform Binary search on an ordered list.
"""


def main():
    list1 = [1, 2, 5, 7, 10, 13, 18, 20, 27]
    num = input("Enter number ")
    l = 0
    r = len(list1)-1

    index = -1

    while l <= r:
        m = l + int((r - l) / 2)
        if num == list1[m]:
            index = m
            break

        elif num < list1[m]:
            r = m - 1

        elif num > list1[m]:
            l = m + 1

    if index != -1:
        print "Found"
    else:
        print "Not found"


if __name__ == '__main__':
    main()
