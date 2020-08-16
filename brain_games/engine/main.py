# TODO: refactor this module as the main entry point for all the scripts

"""Main module for the game logic flow.
use it as a substitute for a brain_games.py"""

from brain_games.scripts.cli import ask
from brain_games.engine.games import brain_calc, \
    brain_even, brain_gcd, brain_prime, brain_progression


GREETINGS_TEXT = 'Welcome to the Brain Games!'

def start_game(game_name):

    print(GREETINGS_TEXT)  # constant greeting

    play_text_intro(game_name)



##################


##################

    use

    # print(game_specific_greeting)

    username = cli.welcome_user()
    return username
