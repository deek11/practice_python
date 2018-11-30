#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script takes a list and returns a new list that contains all
 the elements of the first list minus all the duplicates.
"""
import random


def main():
    # listA = random.sample(range(1, 100), 10)
    listA = [1,2,4,4,3,2,4]
    print listA

    # Using set
    setB = set(listA)
    print setB

    # Using list
    listB = [listA[0]]
    listB = [x for x in listA if x not in listB]

    print listB


if __name__ == '__main__':
    main()
