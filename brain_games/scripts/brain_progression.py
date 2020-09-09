"""Arithmetics progression game"""

from brain_games.engine import main_logic
from brain_games.games import progression


def main():
    main_logic.start_game(progression)


if __name__ == "__main__":
    main()
