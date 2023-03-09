#!/usr/bin/python3

# Define the game rules and guidelines as a string variable:
RULES = """
Welcome to ALU PyQuest!

The goal of this game is to test your knowledge of Python programming language.

You will be presented with a series of questions related to the Python curriculum. The questions will be presented one at a time, starting from beginner's level to advanced level, and you will have a limited time to answer each question.

For each correct answer, you will earn 10 points, and for each incorrect answer or if you run out of time, 5 points will be deducted from your score. You will have 25 seconds for each question.

At the end of the game, your total score will be displayed. Good luck!
"""

# Define a function to play game
def playgame():
    print(RULES)
    ready = input("Are you ready to start the game? Enter(yes/no): ")
    if ready.lower() == "yes":
        print("\nGreat! Let's start the game. \n")
    else:
        print("\nNo problem. See you again!\n")


playgame()
