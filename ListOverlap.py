#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script returns a list that contains only the elements that are common between the lists (without duplicates).
"""

import random


def main():
    list1 = random.sample(range(40), 10)
    list2 = random.sample(range(45), 15)

    print list1
    print list2

    common_list = list()
    for a in list2:
        if a in list1:
            if not a in common_list:
                common_list.append(a)

    print common_list


if __name__ == '__main__':
    main()
