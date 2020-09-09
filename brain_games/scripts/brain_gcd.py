"""brain gcd games run script"""

from brain_games.engine import main_logic
from brain_games.games import gcd


def main():
    main_logic.start_game(gcd)


if __name__ == "__main__":
    main()
