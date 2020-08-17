"""Common functions shared between other scripts."""


import time
from brain_games.scripts import cli
from random import randint, seed


def get_user_input(question=''):
    """
    Ask user for the answer to the param 'question'
    :param: question: text for the question
    :type
    """
    print("Question: ", question)
    user_answer = cli.ask_for_user_input()

    return user_answer


def get_random_number(int_begin, int_end):
    """use function both in brain_calc and brain_even games"""
    seed(time.clock())
    random_number = randint(int_begin, int_end)

    return random_number


def it_casts_to_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_answer_correct(correct_answer, user_input):
    if it_casts_to_int(user_input):
        int_user_input = int(user_input)
    else:
        return False

    if correct_answer == int_user_input:
        return True
    else:
        return False
