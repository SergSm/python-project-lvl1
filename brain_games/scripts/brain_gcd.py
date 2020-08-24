"""brain gcd games run script"""


from brain_games.engine.main import start_game
from brain_games.engine.games import brain_gcd


def main():
    start_game(brain_gcd)


if __name__ == "__main__":
    main()
