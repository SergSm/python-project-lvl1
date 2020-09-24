"""Prime number game"""

from brain_games import shared_logic


# game numbers range
MIN_RANDOM = 1
MAX_RANDOM = 100


DESCRIPTION = 'Answer "yes" if given number is prime. '\
              'Otherwise answer "no".'


def get_question_and_right_answer():

    # get question
    random_number = shared_logic.get_random_number(MIN_RANDOM, MAX_RANDOM)
    question = str(random_number)

    # get right answer
    right_answer = "yes" if is_prime(random_number) else "no"

    # return
    result = (question, right_answer)

    return result


def is_prime(number):

    if number <= 1:  # edge case
        return False
    else:
        # the destination range won't have delimeter greated than number / 2
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                return False
        return True
