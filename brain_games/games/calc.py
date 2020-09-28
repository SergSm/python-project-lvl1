"""Calculator game."""

from random import choice
from brain_games import random_wrapper

OPERATIONS = ['+', '-', '*', '/']


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_right_answer():

    random_operation = choice(OPERATIONS)
    random_number1 = random_wrapper.get_random_number(1, 20)
    random_number2 = random_wrapper.get_random_number(1, 20)

    question = f'{random_number1} {random_operation} {random_number2}'

    arithmetic_execution_result = \
        safe_arithmetic_execution(random_operation,
                                  random_number1,
                                  random_number2)
    result = (question, str(arithmetic_execution_result))

    return result


def safe_arithmetic_execution(operation, *numbers):
    """applies operation to symbols which are supposed to be numbers*"""

    [accumulator, *rest] = numbers

    for character in rest:
        try:
            int(character)
        except ValueError:
            return False

        accumulator = calculate(operation, accumulator, character)

    return accumulator


def calculate(operation, number1, number2):

    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        try:
            result = round((number1 / number2), 2)
        except ZeroDivisionError:
            print("Zero divison error! The second nubmer is zero")
    else:
        raise ValueError('unknown operation ', operation)

    return result
