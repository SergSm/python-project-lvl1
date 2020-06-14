"""main module."""

from .cli import welcome_user


def main():
    """Print data."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
