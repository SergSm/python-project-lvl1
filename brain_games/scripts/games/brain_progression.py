"""Arithmetics progression game"""

from brain_games.scripts import brain_games
from brain_games.scripts.common_functions import get_user_input,\
    get_random_number, print_great_success, \
    print_fail, print_cheers_to, is_answer_correct

NUMBER_OF_SUCCESSFUL_TRIES = 3


def play_brain_progression_game():
    username = brain_games.main('What number is missing in the progression?')

    successful_loops = 0
    while successful_loops < NUMBER_OF_SUCCESSFUL_TRIES:  # main loop

        progression_length = 10
        progression_step = get_random_number(1, 10)
        start_number = get_random_number(1, 10)
        position_of_missing_element = get_random_number(0,
                                                        progression_length - 1)

        arithm_progression = get_arithmetic_progression(progression_length,
                                                        progression_step,
                                                        start_number)

        missing_element = arithm_progression[position_of_missing_element]
        question_text = get_question_text(arithm_progression,
                                          position_of_missing_element)

        user_answer = get_user_input(question=question_text)
        user_is_right = is_answer_correct(missing_element, user_answer)

        if user_is_right:
            print_great_success()
            successful_loops += 1
        else:
            print_fail(wrong_answer=user_answer,
                       correct_answer=missing_element)
            break

    if successful_loops >= NUMBER_OF_SUCCESSFUL_TRIES:
        print_cheers_to(username)


def get_arithmetic_progression(length, step, start_number):

    result_list = []

    # the simplest case with the only one number
    if length == 1:
        result_list.append(start_number)
        return result_list

    current_number = start_number
    for x in range(1, length+1):
        current_number += step
        result_list.append(current_number)

    return result_list


def get_question_text(list_of_values, exclude_element):

    text = ""
    for x in range(0, len(list_of_values)-1):
        if x == exclude_element:
            text += '..' + ' '
        else:
            text += str(list_of_values[x]) + ' '

    return text


if __name__ == "__main__":
    play_brain_progression_game()
