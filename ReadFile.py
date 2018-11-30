#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used to read a .txt file that has a list of a bunch of names,
    count how many of each name there are in the file, and print out the results to the screen.
"""

import codecs


def main():
    with codecs.open('sample.txt', 'r') as source_file:
        line = source_file.readline()
        word_count = dict()

        while line:
            line = line.strip()
            words = line.split(" ")
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

            line = source_file.readline()

        for item in word_count.items():
            print item


if __name__ == '__main__':
    main()
