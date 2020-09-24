"""Main module for the game logic flow."""

from brain_games.cli import ask


COMMON_INTRO_TEXT = 'Welcome to the Brain Games!'

NUMBER_OF_SUCCESSFUL_TRIES = 3  # wins number condition


def play(game):
    """
    Greet the user and start the main loop
    :param game: the game logic module
    :return:
    """

    print(COMMON_INTRO_TEXT)
    print(game.DESCRIPTION)

    username = ask("May I have your name? ")
    print('Hello,', username)

    win_counter = 0  # counts
    while win_counter < NUMBER_OF_SUCCESSFUL_TRIES:  # main loop

        question, right_answer = game.get_question_and_right_answer()
        print("Question: ", question)

        user_answer = ask('Your answer: ')

        if right_answer == user_answer:
            win_counter += 1
            print("Correct!")
        else:  # lose situation
            print(' \'', user_answer,
                  '\' is wrong answer ;(. '
                  'Correct answer was \'', right_answer,
                  '\'')
            print('Let\'s try again, ', username, '!')
            break
    else:
        # all games sessions are successful
        print('Congratulations, ', username, '!')
