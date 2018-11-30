#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Let’s say the word the player has to guess is “EVAPORATE”. For this exercise,
        write the logic that asks a player to guess a letter and
        displays letters in the clue word that were guessed correctly.
"""


def guess_letters(word):
    word = list(word.upper())
    print "_ " * len(word)
    guessed = list("_" * len(word))
    guessed_list = []

    guess_count = 0
    while True:
        letter = raw_input("guess your letter : ").upper()
        if letter in guessed_list:
            print "Already guessed!"
        elif letter in word:
            for i in range(0, len(word)):
                if letter == word[i]:
                    guessed[i] = letter
                    word[i] = '_'
        elif letter not in word:
            guessed_list.append(letter)

        guess_count += 1

        if '_' not in guessed:
            print "\nGuessed correctly! Answer is {}".format(''.join(guessed))
            break

        print ' '.join(guessed)

    print "Number of guesses - {}".format(guess_count)



def main():
    word = raw_input("Enter a word ")
    guess_letters(word)


if __name__ == '__main__':
    main()
