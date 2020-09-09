"""Calculator game run script"""

from brain_games.engine import main_logic
from brain_games.games import calc


def main():
    main_logic.start_game(calc)


if __name__ == "__main__":
    main()
