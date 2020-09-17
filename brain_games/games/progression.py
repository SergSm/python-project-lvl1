"""Arithmetics progression game"""

from brain_games import shared_logic

# game numbers range
MIN_RANDOM = 1
MAX_RANDOM = 10
PROGRESSION_LENGTH = 10  # progression length


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_right_answer():

    # get question
    progression_step = shared_logic.get_random_number(MIN_RANDOM, MAX_RANDOM)
    start_number = shared_logic.get_random_number(MIN_RANDOM, MAX_RANDOM)

    position_of_missing_element = shared_logic.\
        get_random_number(0, PROGRESSION_LENGTH - 1)

    arithm_progression = get_arithmetic_progression(PROGRESSION_LENGTH,
                                                    progression_step,
                                                    start_number)

    question = get_question(arithm_progression,
                            position_of_missing_element)

    # get right answer
    right_answer = get_correct_answer(arithm_progression,
                                      position_of_missing_element)

    # return
    result = (question, right_answer)

    return result


def get_correct_answer(arithm_progression, position_of_missing_element):
    return arithm_progression[position_of_missing_element]


def get_arithmetic_progression(length, step, start_number):

    progression = []

    # the simplest case with the only one number
    if length == 1:
        progression.append(start_number)
        return progression

    current_number = start_number
    for x in range(1, length+1):
        current_number += step
        progression.append(current_number)

    return progression


def get_question(progression, exclude_element_index):

    question = ""
    for x in range(0, len(progression) - 1):
        if x == exclude_element_index:
            question += '..' + ' '
        else:
            question += str(progression[x]) + ' '
    question = question.rstrip()

    return question
