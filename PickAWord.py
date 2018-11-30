#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used a pick a word from a file.
"""
import random


def main():
    print pick_a_word()


def pick_a_word():
    with open('sowpods.txt', 'r') as source_file:
        words = source_file.readlines()

    random_num = random.randint(0, len(words))
    return words[random_num].strip()


if __name__ == '__main__':
    main()
