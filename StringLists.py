#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used to print out whether this string is a palindrome or not.

"""


def main():
    input_string = raw_input()
    length = len(input_string)/2
    is_palindrome = True
    for i in range(0,length):
        if input_string[i] != input_string[len(input_string)-i-1]:
            is_palindrome = False
            break
        continue

    print "Is palindrome : {0}".format(is_palindrome)


if __name__ == '__main__':
    main()