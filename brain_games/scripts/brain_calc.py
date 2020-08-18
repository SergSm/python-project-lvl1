"""Calculator game run script"""

from brain_games.engine.main import start_game
from brain_games.engine.games import brain_calc


def main():
    start_game(brain_calc)


if __name__ == "__main__":
    main()
