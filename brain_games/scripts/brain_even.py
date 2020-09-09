"""Check for parity run script"""

from brain_games.engine import main_logic
from brain_games.games import even


def main():
    main_logic.start_game(even)


if __name__ == "__main__":
    main()
