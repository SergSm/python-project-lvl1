from brain_games.scripts import brain_games
from brain_games.scripts.common_functions import get_user_input,\
    get_random_number, it_casts_to_int, \
    print_great_success, print_fail, print_cheers_to, is_answer_correct

from math import gcd


NUMBER_OF_SUCCESSFUL_TRIES = 3


def play_gcd():
    username = brain_games.main('Find the greatest common'
                                'divisor of given numbers.')

    successful_loops = 0
    while successful_loops < NUMBER_OF_SUCCESSFUL_TRIES:  # main loop

        random_number1 = get_random_number(1, 20)
        random_number2 = get_random_number(1, 20)

        question_text = str(random_number1) + ' ' + str(random_number2)

        user_answer = get_user_input(question=question_text)

        gcd_result = gcd(random_number1, random_number2)
        user_is_right = is_answer_correct(gcd_result, user_answer)

        if user_is_right:
            print_great_success()
            successful_loops += 1
        else:
            print_fail(wrong_answer='yes',
                       correct_answer='no')
            break

    if successful_loops >= NUMBER_OF_SUCCESSFUL_TRIES:
        print_cheers_to(username)


if __name__ == "__main__":
    play_gcd()
