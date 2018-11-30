#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used to return a list that contains only the elements
 that are common between the lists (without duplicates).
"""


def main():
    print "Enter list A \n"
    listA = map(int, raw_input().split())
    print "Enter list B \n"
    listB = map(int, raw_input().split())

    listC = list()
    listC = [x for x in listA if x in listB]
    print listC


if __name__ == '__main__':
    main()