"""Check for parity."""

from brain_games.scripts import brain_games
from brain_games.scripts.common_functions import get_user_input,\
    get_random_number,  print_great_success,\
    print_fail, print_cheers_to


NUMBER_OF_SUCCESSFUL_TRIES = 3


def play_parity_check_game():
    username = brain_games.main('Answer \"yes\" if number even'
                                ' otherwise answer \"no\".')

    successful_loops = 0
    while successful_loops < NUMBER_OF_SUCCESSFUL_TRIES:  # main loop

        random_number = get_random_number(1, 20)
        user_answer = get_user_input(question=random_number)

        user_is_right = is_answer_correct(random_number, user_answer)

        if user_is_right:
            print_great_success()
            successful_loops += 1
        else:
            print_fail(wrong_answer='yes',
                       correct_answer='no')
            break

    if successful_loops >= NUMBER_OF_SUCCESSFUL_TRIES:
        print_cheers_to(username)


def is_answer_correct(number, user_answer):
    if is_even(number) and user_answer == 'yes':
        return True
    elif not is_even(number) and user_answer == 'no':
        return True
    else:
        return False


def is_even(number):
    if (number % 2) == 0:
        return True  # Even
    else:
        return False  # Odd


if __name__ == '__main__':
    play_parity_check_game()
