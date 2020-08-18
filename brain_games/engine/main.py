# TODO: refactor this module as the main entry point for all the scripts

"""Main module for the game logic flow.
use it as a substitute for a brain_games.py"""

import time

from random import randint, seed, choice

from brain_games.scripts.cli import ask
from brain_games.engine.games import brain_calc, \
    brain_even, brain_gcd, brain_prime, brain_progression

COMMON_INTRO_TEXT = 'Welcome to the Brain Games!'

NUMBER_OF_SUCCESSFUL_TRIES = 3  # wins number condition


def start_game(game_name):
    """
    Greet the user and start the main loop
    :param game_name: the game logic module
    :return:
    """

    print(COMMON_INTRO_TEXT)  # constant intro
    brain_calc.show_description()  # show the task of the game

    username = ask("May I have your name?")
    print('Hello,', username)  # greetings

    game_context = {}  # param to transfer session specific data like correct and wrong answer
    victory = execute_game_loop(game_name, game_context)

    if victory:
        print_cheers_to(username)
    else:
        print_fail(wrong_answer=game_context.wrong_answer,
                   correct_answer=game_context.right_answer)


def execute_game_loop(game_name, game_context):
    """
    Execute common game logic flow and return the games session result
    :param game_name: the game logic module
    :return: bool
    """

    victory = True
    successful_loops = 0
    while successful_loops < NUMBER_OF_SUCCESSFUL_TRIES:  # main loop

        question_answer = game_name.get_question__right_answer()

        print("Question: ", question_answer.question)  # show the session question
        user_answer = ask('Your answer: ')  # get user answer to the game session

        if answer_is_correct(user_answer, question_answer.right_answer):
            successful_loops += 1
        else:  # transfer the session specific info to the previous function using context variable
            game_context = {'wrong_answer': user_answer,
                            'correct_answer': question_answer.right_answer,
                            }

            victory = False  # lose

    return victory


# region game_events_prints

def print_great_success():
    print('Correct!')


def print_fail(wrong_answer, correct_answer):
    print(' \'', wrong_answer, '\' is wrong answer ;(. '
                               'Correct answer was \'', correct_answer, '\'')
    print('Let\'s try again, !')


def print_cheers_to(username):
    print('Congratulations, ', username, '!')

# endregion


# region answer_check

def answer_is_correct(input_answer, right_answer):
    filtered_answer = filter_user_input(input_answer)
    return str(right_answer) == str(filtered_answer)


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
