"""Prime number game run script"""

from brain_games.engine import main_logic
from brain_games.games import prime


def main():
    main_logic.start_game(prime)


if __name__ == "__main__":
    main()
