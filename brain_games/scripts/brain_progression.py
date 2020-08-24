"""Arithmetics progression game"""

from brain_games.engine import main_logic
from brain_games.engine.games import brain_progression


def main():
    main_logic.start_game(brain_progression)


if __name__ == "__main__":
    main()
