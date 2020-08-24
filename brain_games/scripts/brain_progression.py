"""Arithmetics progression game"""


from brain_games.engine.main import start_game
from brain_games.engine.games import brain_progression


def main():
    start_game(brain_progression)


if __name__ == "__main__":
    main()
