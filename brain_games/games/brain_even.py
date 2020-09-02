"""Check for parity."""

from brain_games.engine import main_logic

# game numbers range
MIN_RANDOM = 1
MAX_RANDOM = 20


DESCRIPTION = 'Answer "yes" if number even'\
               ' otherwise answer "no".'


def get_question_and_right_answer():
    # get question
    random_number = main_logic.get_random_number(MIN_RANDOM, MAX_RANDOM)
    question = str(random_number)

    # get right answer
    if is_even(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    # return
    result = (question, right_answer)

    return result

def is_even(number):
    if (number % 2) == 0:
        return True  # Even
    else:
        return False  # Odd
