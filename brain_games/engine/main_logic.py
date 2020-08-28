"""Main module for the game logic flow."""

import time
from random import randint, seed, choice

from brain_games.cli import ask


COMMON_INTRO_TEXT = 'Welcome to the Brain Games!'

NUMBER_OF_SUCCESSFUL_TRIES = 3  # wins number condition


def start_game(game_name):
    """
    Greet the user and start the main loop
    :param game_name: the game logic module
    :return:
    """

    print(COMMON_INTRO_TEXT)  # constant intro
    print(game_name.DESCRIPTION)  # show the task of the game

    username = ask("May I have your name? ")
    print('Hello,', username)  # greetings

    victory, game_context = execute_game_loop(game_name)

    if victory:
        print_cheers_to(username)
    else:
        print_fail(wrong_answer=game_context['wrong_answer'],
                   correct_answer=game_context['correct_answer'],
                   username=username)


def execute_game_loop(game_name):
    """
    Execute common game logic flow and return the game session's result
    :param game_name: the game logic module
    :return: bool
    """

    victory = True
    successful_loops = 0
    while successful_loops < NUMBER_OF_SUCCESSFUL_TRIES:  # main loop

        question_answer = game_name.get_question__right_answer()
        # show the session question
        print("Question: ", question_answer['question'])
        # get user answer to the game session
        user_answer = ask('Your answer: ')

        # fill in th e context
        game_context = {'wrong_answer': user_answer,
                        'correct_answer': question_answer['right_answer'],
                        }

        if answer_is_correct(user_answer, question_answer['right_answer']):
            successful_loops += 1
        else:  # transfer the session specific info
            # to the previous function using context variable

            victory = False  # lose
            break

    return victory, game_context


# region game_events_prints

def print_fail(wrong_answer, correct_answer, username):
    print(' \'', wrong_answer, '\' is wrong answer ;(. '
                               'Correct answer was \'', correct_answer, '\'')
    print('Let\'s try again, ', username, '!')


def print_cheers_to(username):
    print('Congratulations, ', username, '!')

# endregion


# region answer_check

def answer_is_correct(input_answer, right_answer):
    # there 2 type of right answers: float and string
    if isinstance(right_answer, float):
        filtered_answer = filter_user_input(input_answer)
        result = (str(right_answer) == str(filtered_answer))
    else:
        result = (str(right_answer) == str(input_answer))

    return result


def filter_user_input(user_answer):
    try:
        user_answer = float(user_answer)
        user_answer = apply_rounding(user_answer)
    except ValueError:
        raise Exception('The input should be a number')

    return user_answer

# endregion


# region math_and_rounding

def apply_rounding(number):
    """common float number rounding function """
    return round(number, 2)


def get_random_number(int_begin, int_end):
    """use function both in brain_calc and brain_even games"""
    seed(time.clock())
    random_number = randint(int_begin, int_end)

    return random_number


def get_random_element(the_list):
    return choice(the_list)


def it_casts_to_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# endregion

