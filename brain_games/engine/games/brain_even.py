"""Check for parity."""

from brain_games.engine import main


# game numbers range
MIN_RANDOM = 1
MAX_RANDOM = 20


def show_description():
    print('Answer \"yes\" if number even'
          ' otherwise answer \"no\".')


def get_question__right_answer():

    # get question
    random_number = main.get_random_number(MIN_RANDOM, MAX_RANDOM)
    question_text = str(random_number)

    # get right answer
    right_answer = get_correct_answer(random_number)

    # return
    result = {'question': question_text,
              'right_answer': right_answer,
              }

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
