"""Arithmetics progression game"""

from brain_games.engine import main_logic


# game numbers range
MIN_RANDOM = 1
MAX_RANDOM = 10
PROGRESSION_LEN = 10


def get_description():
    return 'What number is missing in the progression?'


def get_question__right_answer():

    # get question
    progression_step = main_logic.get_random_number(MIN_RANDOM, MAX_RANDOM)
    start_number = main_logic.get_random_number(MIN_RANDOM, MAX_RANDOM)

    position_of_missing_element = main_logic.get_random_number(0,
                                                         PROGRESSION_LEN - 1)

    arithm_progression = get_arithmetic_progression(PROGRESSION_LEN,
                                                    progression_step,
                                                    start_number)

    question_text = get_question_text(arithm_progression,
                                      position_of_missing_element)

    # get right answer
    right_answer = get_correct_answer(arithm_progression,
                                      position_of_missing_element)

    # return
    result = {'question': question_text,
              'right_answer': right_answer,
              }

    return result


def get_correct_answer(arithm_progression, position_of_missing_element):
    return arithm_progression[position_of_missing_element]


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
