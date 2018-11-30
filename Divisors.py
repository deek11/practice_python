#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script asks the user for a number and
 then prints out a list of all the divisors of that number
"""

def main():
    num = input("Enter number ")
    divisors = list()

    for x in range(1, num+1):
        if num % x == 0:
            divisors.append(x)

    print divisors

if __name__ == '__main__':
    main()