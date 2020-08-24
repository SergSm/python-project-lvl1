"""Prime number game run script"""


from brain_games.engine.main import start_game
from brain_games.engine.games import brain_prime


def main():
    start_game(brain_prime)


if __name__ == "__main__":
    main()
