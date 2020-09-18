"""Find the greatest common divisor game."""

from brain_games import shared_logic

from math import gcd

# game numbers range
MIN_RANDOM = 1
MAX_RANDOM = 20


DESCRIPTION = 'Find the greatest common '\
              'divisor of given numbers.'


def get_question_and_right_answer():

    # get question
    random_number1 = shared_logic.get_random_number(MIN_RANDOM, MAX_RANDOM)
    random_number2 = shared_logic.get_random_number(MIN_RANDOM, MAX_RANDOM)

    question = f'{random_number1} {random_number2}'

    # get right answer
    right_answer = gcd(random_number1, random_number2)

    # return
    result = (question, str(right_answer))

    return result
