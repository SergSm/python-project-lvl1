"""Prime number game"""

from brain_games.scripts import brain_games
from brain_games.engine.common_functions import get_user_input,\
    get_random_number, print_great_success, print_fail, print_cheers_to


NUMBER_OF_SUCCESSFUL_TRIES = 3


def play_brain_prime():
    username = brain_games.main('Answer \"yes\" if given number is prime. '
                                'Otherwise answer \"no\".')

    successful_loops = 0
    while successful_loops < NUMBER_OF_SUCCESSFUL_TRIES:  # main loop

        random_number = get_random_number(1, 100)

        is_prime_number = is_prime(random_number)

        user_answer = get_user_input(question=random_number)
        user_is_right = is_answer_correct(is_prime_number,
                                          user_input=user_answer)

        correct_answer = get_text_answer(is_prime_number)

        if user_is_right:
            print_great_success()
            successful_loops += 1
        else:
            print_fail(wrong_answer=user_answer,
                       correct_answer=correct_answer)
            break

    if successful_loops >= NUMBER_OF_SUCCESSFUL_TRIES:
        print_cheers_to(username)


def get_text_answer(is_prime_number):
    if is_prime_number:
        return 'yes'
    else:
        return 'no'


def is_answer_correct(is_prime_number, user_input):

    if is_prime_number and user_input == 'yes':
        return True
    elif not is_prime_number and user_input == 'no':
        return True
    else:
        return False


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
