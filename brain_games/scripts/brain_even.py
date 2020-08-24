"""Check for parity run script"""

from brain_games.engine import main_logic
from brain_games.engine.games import brain_even


def main():
    main_logic.start_game(brain_even)


if __name__ == "__main__":
    main()
