"""Check for parity."""

from brain_games.scripts import brain_games, cli
from random import randint


NUMBER_OF_SUCCESSFUL_TRIES = 3


def play_parity_check_game():
    username = brain_games.main()

    successful_loops = 0
    while successful_loops < NUMBER_OF_SUCCESSFUL_TRIES:  # main loop

        random_number = randint(1, 20)
        print("Question: ", random_number)
        user_answer = cli.ask_for_user_input()

        user_is_right = is_answer_correct(random_number, user_answer)

        if user_is_right:
            print('Correct!')
            successful_loops += 1
        else:
            print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
            print('Let\'s try again, !')
            break

    if successful_loops >= NUMBER_OF_SUCCESSFUL_TRIES:
        print('Congratulations, ', username, '!')


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
