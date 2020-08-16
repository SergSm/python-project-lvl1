# TODO: refactor this module as the main entry point for all the scripts

"""Main module for the game logic flow.
use it as a substitute for a brain_games.py"""

from brain_games.scripts import cli


def start(game_specific_greeting):
    print('Welcome to the Brain Games!')

    print(game_specific_greeting)

    username = cli.welcome_user()
    return username
