#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" The user, will have in your head a number between 0 and 100. The program will guess a number,
    and you, the user, will say whether it is too high, too low, or your number.
    At the end of this exchange, your program should print out how many guesses it took to get your number.
"""


def main():
    l = 0
    r = 100
    guess = -1
    m = (l + r) / 2
    num_of_loops = 0
    while True:
        m = (r + l) / 2
        guess = input("Your number is {0}. Press :- 1 - Correct Guess , 2 - Too High, 3 - Too Low ".format(m))

        if guess == 1:
            print "We found your number! It is {0}".format(m)
            break
        elif guess == 2:
            r = m - 1
        else:
            l = m + 1
        num_of_loops += 1

    print "Total rounds - {0}".format(num_of_loops)


if __name__ == '__main__':
    main()
