"""Calculator game run script"""

from brain_games.engine import main_logic
from brain_games.games import brain_calc


def main():
    main_logic.start_game(brain_calc)


if __name__ == "__main__":
    main()
