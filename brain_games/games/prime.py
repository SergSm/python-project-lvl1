"""Prime number game"""

from brain_games import shared_logic
import brain_games.games.prime as game


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

    if number <= 1:  # prime number is always greater than 1
        # 0 and negative numbers are not prime numbers
        number_is_divisible = False
    else:
        number_is_divisible = not is_divisible(number)

    return number_is_divisible


def is_divisible(number):

    divisibiliy_trigger = False
    for i in range(2, number):
        if (number % i) == 0:
            divisibiliy_trigger = True

    return divisibiliy_trigger
