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

    print(COMMON_INTRO_TEXT)  # constant intro
    print(game.DESCRIPTION)  # show the task of the game

    username = ask("May I have your name? ")
    print('Hello,', username)  # greetings

    win_counter = 0  # counts  
    while win_counter < NUMBER_OF_SUCCESSFUL_TRIES:  # main loop

        question, right_answer = game.get_question_and_right_answer()
        # show the session question
        print("Question: ", question)
        # get user answer to the game session
        user_answer = ask('Your answer: ')

        # compare user answer and right answer
        if isinstance(right_answer, float):
            try:
                user_answer = round(float(user_answer), 2)
            except ValueError:
                raise Exception('The input should be a number')

        game_session_victory = (str(right_answer) == str(user_answer))

        if game_session_victory:
            win_counter += 1
        else:
            break

    if win_counter < NUMBER_OF_SUCCESSFUL_TRIES:  # lose situation
        print(' \'', user_answer,
              '\' is wrong answer ;(. '
              'Correct answer was \'', right_answer,
              '\'')
        print('Let\'s try again, ', username, '!')
    else:  # win
        print('Congratulations, ', username, '!')
