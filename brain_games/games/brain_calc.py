"""Calculator game."""

from brain_games.engine import main_logic
from random import choice

OPERATIONS = ['+', '-', '*', '/']


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_right_answer():

    # get question
    random_operation = choice(OPERATIONS)
    random_number1 = main_logic.get_random_number(1, 20)
    random_number2 = main_logic.get_random_number(1, 20)

    question_text = str(random_number1) + random_operation
    question_text += str(random_number2)

    # get right answer
    arithmetic_result = float(safe_arithmetic_execution(random_operation,
                                                        random_number1,
                                                        random_number2))
    # return
    result = (question_text, arithmetic_result)

    return result


# TODO: provide more detailed information about purpose of this function
def safe_arithmetic_execution(operation, *numbers):
    """applies operation to numbers*"""

    accumulator = numbers[0]  # assign to the very first value

    for number in numbers[1:]:
        if main_logic.it_casts_to_int(number):  # check if param casts to int
            accumulator = calculate(operation, accumulator, number)

    return accumulator


def calculate(operation, number1, number2):
    try:
        if operation == '+':
            number1 = number1 + number2
        elif operation == '-':
            number1 = number1 - number2
        elif operation == '*':
            number1 = number1 * number2
        elif operation == '/':
            number1 = round((number1 / number2), 2)
    except ValueError:
        return False
    return number1
