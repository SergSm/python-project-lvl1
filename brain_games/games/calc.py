"""Calculator game."""

from random import choice
from brain_games import shared_logic

OPERATIONS = ['+', '-', '*', '/']


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_right_answer():

    # get question
    random_operation = choice(OPERATIONS)
    random_number1 = shared_logic.get_random_number(1, 20)
    random_number2 = shared_logic.get_random_number(1, 20)

    question = f'{random_number1} {random_operation} {random_number2}'

    # get right answer
    arithmetic_execution_result = \
        safe_arithmetic_execution(random_operation,
                                  random_number1,
                                  random_number2)
    # return
    # Attention! The result contains not only the right answer but also
    # the question so the engine function can render it
    result = (question, str(arithmetic_execution_result))

    return result


def safe_arithmetic_execution(operation, *numbers):
    """applies operation to numbers*"""

    accumulator = numbers[0]  # assign to the very first value

    for number in numbers[1:]:
        if shared_logic.it_casts_to_int(number):  # check if param casts to int
            accumulator = calculate(operation, accumulator, number)

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


def it_casts_to_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
