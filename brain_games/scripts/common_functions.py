"""Common functions shared between other scripts."""

from brain_games.scripts import cli
from random import randint

def get_user_input(question=''):
    """
    Ask user for the answer to the param 'question'
    :param: question: text for the question
    :type
    """
    print("Question: ", question)
    user_answer = cli.ask_for_user_input()

    return user_answer


def get_random_number(int_begin, int_end):
    """use function both in brain_calc and brain_even games"""
    random_number = randint(int_begin, int_end)

    return random_number


def it_casts_to_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def print_great_success():
    print('Correct!')


def print_fail(wrong_answer, correct_answer):
    print('\'''', wrong_answer ,'''\' is wrong answer ;(. Correct answer was \'''', correct_answer) # ,'' \'.') # TODO
    print('Let\'s try again, !')


def print_cheers_to(username):
    print('Congratulations, ', username, '!')
