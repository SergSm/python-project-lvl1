"""Command line input module."""

import prompt


def welcome_user():
    """Ask to input name and greet user."""
    username = ask_for_username()
    print('Hello,', username)
    return username


def ask_for_username():
    name = prompt.string('May I have your name? ')
    return name


def ask_for_user_input():
    """User input"""
    user_answer = prompt.string('Your answer: ')
    return user_answer
