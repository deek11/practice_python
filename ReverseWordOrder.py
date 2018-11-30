#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used reverse a string
"""


def main():
    input_string = raw_input("Enter some text")
    words = input_string.split(" ")
    output_string = " ".join(words[::-1])
    print output_string


if __name__ == '__main__':
    main()
