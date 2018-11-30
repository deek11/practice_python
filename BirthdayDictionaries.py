#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used for implementing dictionary
"""
import json


def main():
    birthday_diary = {
        "Homer": "12/05/1952",
        "Lisa": "09/12/1995",
        "Bart": "28/07/1991"
    }

    name = raw_input("Enter name ")

    print birthday_diary.get(name, "no record found")


if __name__ == '__main__':
    main()
