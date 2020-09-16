"""
Author: Morgan McCarley
Program: validation_with_try.py
Date: 9/15/2020

program prompts for three test scores and returns the average to the user.
"""
NUMBER_TESTS = 4


def average(score1, score2, score3, score4):
    if score1 < 0 or score2 < 0 or score3 < 0:
        raise ValueError
    return float((score1 + score2 + score3)/NUMBER_TESTS)


if __name__ == '__main__':
    lastName = input("Enter your last name:")
    firstName = input("Enter your first name: ")
    age = input("Enter your age: ")
    first_score = input("Enter your first score: ")
    second_score = input("Enter your second score: ")
    third_score = input("Enter your third score: ")
    fourth_score = input("Enter your fourth score: ")
    try:
        average_scores = average(int(first_score), int(second_score),
                                 int(third_score), int(fourth_score))
    except ValueError:
        print("Please enter only positive scores!")
    else:
        print("{}, {} age: {} average grade: {}".format(lastName, firstName, age, average_scores))


