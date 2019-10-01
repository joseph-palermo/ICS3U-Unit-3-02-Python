#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: Sep 2019
# This program adds integers


import constants


def main():
    # This function asks the user to guess the number

    # Input
    guess = int(input("Guess the number between 1 & 9 (integer): "))
    print("")

    # process
    if guess == constants.CORRECT_NUMBER:
        # Output
        print("You guessed the number!")


if __name__ == "__main__":
    main()
