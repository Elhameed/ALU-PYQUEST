#!/usr/bin/python3

import time
import random
import beginner_questions
import medium_questions
import advanced_questions

# Define the game rules and guidelines as a string variable:
RULES = """
Welcome to ALU PyQuest!

The goal of this game is to test your knowledge of Python programming language.

You will be presented with a series of questions related to the Python curriculum. The questions will be presented one at a time, starting from beginner's level to advanced level, and you will have a limited time to answer each question.

For each correct answer, you will earn 10 points, and for each incorrect answer or if you run out of time, 5 points will be deducted from your score. You will have 25 seconds for each question.

In total, you will be asked 12 questions, 4 questions for each level of difficulty.

At the end of the game, your total score will be displayed. Good luck!
"""

#function to load and save high scores to a file
HIGH_SCORES_FILE = 'high_scores.txt'

def load_high_scores():
    high_scores = []
    try:
        with open(HIGH_SCORES_FILE, 'r') as f:
            for line in f:
                name, score = line.strip().split(',')
                high_scores.append((name, int(score)))
    except FileNotFoundError:
        pass  # If the file doesn't exist, return an empty list
    return high_scores

def save_high_scores(high_scores):
    with open(HIGH_SCORES_FILE, 'w') as f:
        for name, score in high_scores:
            f.write(f"{name},{score}\n")

#function to generate random questions from beginner to advanced
BEGINNER_PROBLEMS = beginner_questions.PROBLEM_SETS
MEDIUM_PROBLEMS = medium_questions.PROBLEM_SETS
ADVANCED_PROBLEMS = advanced_questions.PROBLEM_SETS

def generate_problem_sets(difficulty_level):
    if difficulty_level == 'beginner':
        return random.sample(BEGINNER_PROBLEMS, k=4)
    elif difficulty_level == 'medium':
        return random.sample(MEDIUM_PROBLEMS, k=4)
    elif difficulty_level == 'advanced':
        return random.sample(ADVANCED_PROBLEMS, k=4)

# Define a function to play game
def playgame():
    #print initial message
    print("Loading the game...")
    time.sleep(2)
    print(RULES)

    #load and display high scores
    high_scores = load_high_scores()
    if high_scores:
        print("High scores:")
        for i, (name, score) in enumerate(high_scores[:5]):
            print(f"{i+1}. {name}: {score}")
    
    #start the game
    ready = input("Are you ready to start the game? Enter(yes/no): ")    
    if ready.lower() == "yes":
        print("\nGreat! Let's start the game. \n")
        print("Loading the game...")
        time.sleep(1.5)
        print("Please wait...")
        time.sleep(1.5)
        print("Ready!")
        time.sleep(1.5)

        difficulty_levels = ['beginner', 'medium', 'advanced']
        score = 0
        for level in difficulty_levels:
            problem_set = generate_problem_sets(level)
            print(f"\nLevel: {level.capitalize()}")
            counter = 1
            for problem in problem_set:
                print(f"\n{counter}. {problem['question']}")
                for option in problem['options']:
                    print(f"{option}: {problem['options'][option]}")
                start_time = time.time()
                answer = input("Enter your answer: ")
                elapsed_time = time.time() - start_time
                if answer.strip().lower() == problem['answer'].lower() and elapsed_time <= 25:
                    score += 10
                    print("Correct!")
                elif elapsed_time > 25:
                    score -= 5
                    print(f"The correct answer is: {problem['answer']}")
                    print(f"You took too long to answer the question. Time elapsed: {elapsed_time:.2f} seconds")
                else:
                    score -= 5
                    print(f"Incorrect! The correct answer is: {problem['answer']}")
                print(f"Your current score is: {score}")
                counter += 1
                time.sleep(1)
        print(f"\nYour final score is: {score}")

        #Stores user score
        name = input("Enter your name: ")
        high_scores.append((name, score))
        high_scores.sort(key=lambda x: x[1], reverse=True)
        if len(high_scores) > 5:
            high_scores = high_scores[:5]
        save_high_scores(high_scores)

        #asks user to view high score
        view_high_scores = input("\nDo you want to view high scores? Enter(yes/no): ")
        if view_high_scores.lower() == "yes":
            print("\nHigh scores:")
            for i, (name, score) in enumerate(high_scores[:5]):
                print(f"{i+1}. {name}: {score}")

        play_again = input("\nDo you want to play again? Enter(yes/no): ")
        while play_again.lower() == 'yes':
            print("Loading the game...")
            time.sleep(1.5)
            print("Please wait...")
            time.sleep(1.5)
            print("Ready!")
            time.sleep(1.5)

            difficulty_levels = ['beginner', 'medium', 'advanced']
            score = 0
            for level in difficulty_levels:
                problem_set = generate_problem_sets(level)
                print(f"\nLevel: {level.capitalize()}")
                counter = 1
                for problem in problem_set:
                    print(f"\n{counter}. {problem['question']}")
                    for option in problem['options']:
                        print(f"{option}: {problem['options'][option]}")
                    start_time = time.time()
                    answer = input("Enter your answer: ")
                    elapsed_time = time.time() - start_time
                    if answer.strip().lower() == problem['answer'].lower() and elapsed_time <= 25:
                        score += 10
                        print("Correct!")
                    elif elapsed_time > 25:
                        score -= 5
                        print(f"The correct answer is: {problem['answer']}")
                        print(f"You took too long to answer the question. Time elapsed: {elapsed_time:.2f} seconds")
                    else:
                        score -= 5
                        print(f"Incorrect! The correct answer is: {problem['answer']}")
                    print(f"Your current score is: {score}")
                    counter += 1
                    time.sleep(1)
            print(f"\nYour final score is: {score}")

            #store users score
            name = input("Enter your name: ")
            high_scores.append((name, score))
            high_scores.sort(key=lambda x: x[1], reverse=True)
            if len(high_scores) > 5:
                high_scores = high_scores[:5]
            save_high_scores(high_scores)

            #asks user to view high core
            view_high_scores = input("\nDo you want to view high scores? Enter(yes/no): ")
            if view_high_scores.lower() == "yes":
                print("\nHigh scores:")
                for i, (name, score) in enumerate(high_scores[:5]):
                    print(f"{i+1}. {name}: {score}")

            play_again = input("\nDo you want to play again? Enter(yes/no): ")
        else:
            print("\nThank you for playing! Goodbye.")
    else:
        print("\nNo problem. See you again!\n")

playgame()
