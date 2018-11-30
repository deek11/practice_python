#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used for creating dictionary from JSON file.
"""
import json


def main():
    with open('birthdays.txt', 'r') as sfile:
        birthday_diary = json.load(sfile)
        name = raw_input("Enter name ")

        print birthday_diary.get(name, "no record found")


if __name__ == '__main__':
    main()
