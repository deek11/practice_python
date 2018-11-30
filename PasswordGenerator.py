#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used to generate a random password
"""
import random
import string


def main():
    length = random.randint(8, 15)
    s = string.ascii_letters + string.digits + string.punctuation
    p = "".join(random.sample(s, length))
    print p


if __name__ == '__main__':
    main()
