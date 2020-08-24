"""Check for parity."""

from brain_games.engine import main
import brain_games.engine.games.brain_even as game

# game numbers range
MIN_RANDOM = 1
MAX_RANDOM = 20


def get_description():
    return 'Answer \"yes\" if number even'\
           ' otherwise answer \"no\".'


def get_question__right_answer():

    return main.question_answer_wrapper(MIN_RANDOM, MAX_RANDOM, game)


def get_correct_answer(number):
    if is_even(number):
        return 'yes'
    else:
        return 'no'


def is_even(number):
    if (number % 2) == 0:
        return True  # Even
    else:
        return False  # Odd
