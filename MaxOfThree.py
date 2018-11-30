#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used find max of three numbers.
"""


def main():
    x, y, z = [int(x) for x in raw_input("Enter 3 integers").split(" ")]
    if x > y:
        if x > z:
            max = x
        else:
            max = z
    else:
        if y > z:
            max = y
        else:
            max = z

    print "Max - {0}".format(max)


if __name__ == '__main__':
    main()
