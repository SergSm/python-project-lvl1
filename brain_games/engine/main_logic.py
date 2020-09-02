"""Main module for the game logic flow."""


from brain_games.cli import ask


COMMON_INTRO_TEXT = 'Welcome to the Brain Games!'

NUMBER_OF_SUCCESSFUL_TRIES = 3  # wins number condition


def start_game(game_name):
    """
    Greet the user and start the main loop
    :param game_name: the game logic module
    :return:
    """

    print(COMMON_INTRO_TEXT)  # constant intro
    print(game_name.DESCRIPTION)  # show the task of the game

    username = ask("May I have your name? ")
    print('Hello,', username)  # greetings

    victory, game_context = execute_game_loop(game_name)

    if victory:
        print('Congratulations, ', username, '!')
    else:
        print(' \'', game_context['wrong_answer'],
              '\' is wrong answer ;(. '
              'Correct answer was \'', game_context['correct_answer'],
              '\'')
        print('Let\'s try again, ', username, '!')


def execute_game_loop(game_name):
    """
    Execute common game logic flow and return the game session's result
    :param game_name: the game logic module
    :return: bool
    """

    victory = True
    successful_loops = 0
    while successful_loops < NUMBER_OF_SUCCESSFUL_TRIES:  # main loop

        question_answer = game_name.get_question_and_right_answer()
        # show the session question
        print("Question: ", question_answer[0])
        # get user answer to the game session
        user_answer = ask('Your answer: ')

        # fill in the context
        game_context = {'wrong_answer': user_answer,
                        'correct_answer': question_answer[1],
                        }

        # compare user answer and right answer
        if isinstance(question_answer[1], float):
            try:
                user_answer = round(float(user_answer), 2)
            except ValueError:
                raise Exception('The input should be a number')

        game_session_victory = (str(question_answer[1]) == str(user_answer))

        if game_session_victory:
            successful_loops += 1
        else:  # transfer the session specific info
            # to the previous function using context variable
            victory = False  # lose
            break

    return victory, game_context
