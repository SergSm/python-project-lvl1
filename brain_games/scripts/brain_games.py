"""Main module."""

from brain_games.scripts import cli


def main():
    print('Welcome to the Brain Games!')
    print("Answer "'yes'" if number even otherwise answer "'no'".")
    username = cli.welcome_user()
    return username


if __name__ == '__main__':
    main()
