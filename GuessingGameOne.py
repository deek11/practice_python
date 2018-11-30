#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
"""

import random


def main():
    print "The Guessing Game!"
    user_command = ""
    correct_guess = 0

    while user_command != "exit":
        random_num = random.randint(1,9)
        user_guess = input("Guess a number between 1 to 9 \n")
        if random_num == user_guess:
            correct_guess += 1
            print "Correct guess. Congratulations, you win! "
        else:
            print "Incorrect guess. Sorry, you lost this round. Better luck next time. "

        user_command = raw_input("Type exit to quit \n")

    print "Your score - {0}".format(correct_guess)


if __name__ == '__main__':
    main()




