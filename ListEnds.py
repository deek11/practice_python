#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
    makes a new list of only the first and last elements of the given list.
"""
import random


def main():
    sample_list = random.sample(range(1, 100), 5)
    print sample_list

    new_list = []
    new_list.append(sample_list[0])
    new_list.append(sample_list[len(sample_list)-1])

    print new_list


if __name__ == '__main__':
    main()