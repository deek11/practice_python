#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used to determine whether the number is prime or not.
"""

import UserInputHelper
import math


def main():
    num = UserInputHelper.get_integer()
    prime = True
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            prime = False
            break

    print("{0} is prime".format(num) if prime else "{0} is not prime".format(num))


if __name__ == '__main__':
    main()


