"""Check for parity."""

from brain_games import random_wrapper

# game numbers range
MIN_RANDOM = 1
MAX_RANDOM = 20


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def get_question_and_right_answer():
    random_number = random_wrapper.get_random_number(MIN_RANDOM, MAX_RANDOM)
    question = str(random_number)

    right_answer = 'yes' if random_number % 2 == 0 else 'no'

    result = (question, right_answer)

    return result
