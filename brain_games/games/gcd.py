"""Find the greatest common divisor game."""

from brain_games import random_wrapper

from math import gcd

# game numbers range
MIN_RANDOM = 1
MAX_RANDOM = 20


DESCRIPTION = 'Find the greatest common '\
              'divisor of given numbers.'


def get_question_and_right_answer():

    random_number1 = random_wrapper.get_random_number(MIN_RANDOM, MAX_RANDOM)
    random_number2 = random_wrapper.get_random_number(MIN_RANDOM, MAX_RANDOM)

    question = f'{random_number1} {random_number2}'

    right_answer = gcd(random_number1, random_number2)

    result = (question, str(right_answer))

    return result
