"""Arithmetics progression game"""

from brain_games import random_wrapper

# game numbers range
MIN_RANDOM = 1
MAX_RANDOM = 10
PROGRESSION_LENGTH = 10


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_right_answer():

    progression_step = random_wrapper.get_random_number(MIN_RANDOM, MAX_RANDOM)
    start_number = random_wrapper.get_random_number(MIN_RANDOM, MAX_RANDOM)

    progression = [start_number + progression_step*counter
                   for counter in range(PROGRESSION_LENGTH)]

    position_of_missing_element = random_wrapper.\
        get_random_number(0, PROGRESSION_LENGTH - 1)

    question = get_question(progression,
                            position_of_missing_element)

    right_answer = progression[position_of_missing_element]

    result = (question, str(right_answer))

    return result


def get_question(progression, excluded_element_index):

    question = ""
    for x in range(0, len(progression) - 1):
        if x == excluded_element_index:
            question += '.. '  # SPACE HERE!
        else:
            question += str(progression[x]) + ' '

    return question.rstrip()
