"""Find the greatest common divisor game."""

from brain_games.engine import main_logic

from math import gcd

# game numbers range
MIN_RANDOM = 1
MAX_RANDOM = 20


def get_description():
    return 'Find the greatest common '\
           'divisor of given numbers.'


def get_question__right_answer():

    # get question
    random_number1 = main_logic.get_random_number(MIN_RANDOM, MAX_RANDOM)
    random_number2 = main_logic.get_random_number(MIN_RANDOM, MAX_RANDOM)

    question_text = str(random_number1) + ' ' + str(random_number2)

    # get right answer
    right_answer = get_correct_answer(random_number1, random_number2)

    # return
    result = {'question': question_text,
              'right_answer': right_answer,
              }

    return result


def get_correct_answer(random_number1, random_number2):
    return gcd(random_number1, random_number2)
