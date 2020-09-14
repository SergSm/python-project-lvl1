"""Additional module for common functions used in games"""


import time
from random import randint, seed


def get_random_number(int_begin, int_end):
    """used in all games"""
    seed(time.clock())
    random_number = randint(int_begin, int_end)

    return random_number


def it_casts_to_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_win(right_answer, user_answer):
    # compare user answer and right answer
    if isinstance(right_answer, float):
        try:
            user_answer = round(float(user_answer), 2)
        except ValueError:
            raise Exception('The input should be a number')

    return str(right_answer) == str(user_answer)
