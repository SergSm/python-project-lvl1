# TODO: refactor this module as the main entry point for all the scripts

"""Main module for the game logic flow.
use it as a substitute for a brain_games.py"""


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

    victory = game_loop(game_name)

    if victory:
        print_cheers_to(username)


def game_loop(game_name):
    """
    Execute common game logic flow
    :param game_name: the game logic module
    :return:
    """

    victory = True
    successful_loops = 0
    while successful_loops < NUMBER_OF_SUCCESSFUL_TRIES:  # main loop

        question_answer = game_name.get_question_answer()

        print("Question: ", question_answer.question)  # show the session question
        user_answer = ask('Your answer: ')  # get the user answer to the game session

        if answer_is_correct(user_answer, question_answer.right_answer):
            successful_loops += 1
        else:
            print_fail(wrong_answer=user_answer,
                       correct_answer=question_answer.right_answer)

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


#######################################################################################


def answer_is_correct(input_answer, right_answer):
    filtered_answer = filter_user_input(input_answer)
    return str(right_answer) == str(filtered_answer)


def apply_rounding(number):
    return round(number, 2)


def filter_user_input(user_answer):
    try:
        user_answer = float(user_answer)
        user_answer = apply_rounding(user_answer)
    except ValueError:
        raise Exception('The input should be a number')

    return user_answer




