"""Prime number game"""

from brain_games.engine import main_logic
import brain_games.engine.games.brain_prime as game


# game numbers range
MIN_RANDOM = 1
MAX_RANDOM = 100


def get_description():
    return 'Answer \"yes\" if given number is prime. '\
           'Otherwise answer \"no\".'


def get_question__right_answer():

    return main_logic.question_answer_wrapper(MIN_RANDOM, MAX_RANDOM, game)


def get_correct_answer(number):

    is_prime_number = is_prime(number)

    if is_prime_number:
        return 'yes'
    else:
        return 'no'


def is_prime(number):

    number_is_divisible = False

    if number != 1:     # prime number is always greater than 1
        number_is_divisible = not is_divisible(number)
    else:
        number_is_divisible = False  # 1 is a special case

    return number_is_divisible


def is_divisible(number):

    divisibiliy_trigger = False
    for i in range(2, number):
        if (number % i) == 0:
            divisibiliy_trigger = True

    return divisibiliy_trigger
