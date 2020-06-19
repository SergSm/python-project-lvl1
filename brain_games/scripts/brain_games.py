"""Main module."""

from brain_games.scripts import cli


def main(game_specific_greeting):
    print('Welcome to the Brain Games!')

    print(game_specific_greeting)

    username = cli.welcome_user()
    return username


if __name__ == '__main__':
    main()
