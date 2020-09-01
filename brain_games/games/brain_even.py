"""Check for parity."""

from brain_games.engine import main_logic
import brain_games.games.brain_even as game

# game numbers range
MIN_RANDOM = 1
MAX_RANDOM = 20


DESCRIPTION = 'Answer \"yes\" if number even'\
               ' otherwise answer \"no\".'


def get_question_and_right_answer():
    # get question
    random_number = main_logic.get_random_number(MIN_RANDOM, MAX_RANDOM)
    question_text = str(random_number)

    # get right answer
    right_answer = game.get_correct_answer(random_number)

    # return
    result = (question_text, right_answer)

    return result


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
