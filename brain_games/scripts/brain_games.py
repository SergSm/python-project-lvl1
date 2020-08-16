# TODO: 1 Eradicate this module

"""Main module. Entry point"""

from brain_games.scripts import cli


#def main(game_specific_greeting):
def main(game_type):

    greet_user() # Greet user anyway
    
    # TODO: printing game-specific greeting
    #print(game_specific_greeting)

    username = cli.welcome_user()
    return username


if __name__ == '__main__':
    main()


def greet_user()
    print('Welcome to the Brain Games!')