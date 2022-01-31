


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#


# ASK FOR USER INPUT


user_choice = input("Please choose one of: 'rock', 'paper', 'scissors': ")

print("USER CHOSE:", user_choice)


# VALIDATIONS



# COMPUTER CHOICE
# https://docs.python.org/3/library/random.html#random.choice
# https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
# https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/modules/random.md

#import random
from random import choice

options = ["rock", "paper", "scissors"]

#computer_choice = random.choice(options)
computer_choice = choice(options)

print("COMPUTER CHOSE:", computer_choice)





# DETERMINE THE WINNER

# option a) nested IF statements
# adapted from eugenie in Slack

if user_choice == computer_choice:
    print("Both players played", user_choice, "It's a tie!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock. You won!")
    else:
        print("Scissors cuts paper. You lost! It's ok.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper. You won!")
    else:
        print("Rock crushes scissors. You lost! It's ok.")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock crushes scissors. You won!")
    else:
        print("Paper covers rock You lost! It's ok.")


# FINAL RESULTS
