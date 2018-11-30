#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This script is used to Make a two-player Rock-Paper-Scissors game.
"""


def main():
    print "Rock Paper Scissors!"
    print "Rules :- \n" \
          "0 - Rock \n" \
          "1 - Paper \n" \
          "2 - Scissors"

    continue_play = "y"
    while continue_play == "y":
        player1 = input("Player 1, enter your move ")
        player2 = input("Player 2, enter your move ")

        sinput1 = get_object(player1)
        sinput2 = get_object(player2)

        print "Player1 - {0} | Player2 - {1} \n".format(sinput1, sinput2)

        if (sinput1 == "Invalid Input") or (sinput2 == "Invalid Input"):
            print "Invalid Input"
        else:
            if (player1 == 0 and player2 == 2) or (player1 == 1 and player2 == 0) or (player1 == 2 and player2 == 1):
                winner = "Player 1"
                print winner
            elif (player2 == 0 and player2 == 2) or (player2 == 1 and player1 == 0) or (player2 == 2 and player1 == 1):
                winner = "Player 2"
            else:
                winner = "None. It is tie!"

        print "The winner is {0} \n".format(winner)

        continue_play = raw_input("Press y to continue , n to exit.. \n")


def get_object(user_input):
    if user_input == 0:
        return "Rock"
    elif user_input == 1:
        return "Paper"
    elif user_input == 2:
        return "Scissors"
    else:
        return "Invalid Input"


if __name__ == '__main__':
    main()



