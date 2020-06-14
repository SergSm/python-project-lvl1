"""User unput module."""

import prompt


def welcome_user():
    """Greet user and ask to input."""
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
