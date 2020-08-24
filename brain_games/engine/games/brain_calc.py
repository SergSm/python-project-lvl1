"""Calculator game."""

from brain_games.engine import main_logic


OPERATIONS = ('+', '-', '*', '/')


def get_description():
    return 'What is the result of the expression?'


def get_question__right_answer():

    # get question
    random_operation = main_logic.get_random_element(OPERATIONS)
    random_number1 = main_logic.get_random_number(1, 20)
    random_number2 = main_logic.get_random_number(1, 20)

    question_text = str(random_number1) + random_operation
    question_text += str(random_number2)

    # get right answer
    arithmetic_result = float(safe_arithmetic_execution(random_operation,
                                                        random_number1,
                                                        random_number2))
    # return
    result = {'question': question_text,
              'right_answer': arithmetic_result,
              }

    return result


def safe_arithmetic_execution(operation, *numbers):
    """applies operation to numbers*"""

    accumulator = numbers[0]  # assign to the very first value

    for number in numbers[1:]:
        if main_logic.it_casts_to_int(number):  # check if param casts to integer
            accumulator = apply_operation(operation, accumulator, number)

    return accumulator


def apply_operation(operation, accumulator, number):
    try:
        if operation == '+':
            accumulator = accumulator + number
        elif operation == '-':
            accumulator = accumulator - number
        elif operation == '*':
            accumulator = accumulator * number
        elif operation == '/':
            accumulator = main_logic.apply_rounding(accumulator / number)
    except ValueError:
        return False
    return accumulator
