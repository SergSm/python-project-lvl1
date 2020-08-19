"""Check for parity run script"""


from brain_games.engine.main import start_game
from brain_games.engine.games import brain_even


def main():
    start_game(brain_even)


if __name__ == "__main__":
    main()
