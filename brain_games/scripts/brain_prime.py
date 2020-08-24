"""Prime number game run script"""

from brain_games.engine import main_logic
from brain_games.engine.games import brain_prime


def main():
    main_logic.start_game(brain_prime)


if __name__ == "__main__":
    main()
