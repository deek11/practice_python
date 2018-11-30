#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used create the game of Hangman
"""
import PickAWord
import GuessLetters


def play_hangman():
    word = PickAWord.pick_a_word()
    print word
    GuessLetters.guess_letters(word)


def main():
    play = 'y'
    while play == 'y':
        play_hangman()
        play = raw_input("Do you want to play another round? y - yes, n - no ")


if __name__ == '__main__':
    main()
