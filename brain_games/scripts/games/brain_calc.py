"""Calculator game."""

from brain_games.scripts import brain_games
from brain_games.scripts.common_functions import get_user_input,\
    get_random_number, it_casts_to_int, \
    print_great_success, print_fail, print_cheers_to

NUMBER_OF_SUCCESSFUL_TRIES = 3


def play_calc_game():
    username = brain_games.main()

    successful_loops = 0
    while successful_loops < NUMBER_OF_SUCCESSFUL_TRIES:  # main loop

        random_operation = get_random_operation_sign()
        random_number1 = get_random_number(1, 20)
        random_number2 = get_random_number(1, 20)

        question_text = str(random_number1) + random_operation
        question_text += str(random_number2)

        arithmetic_result = float(safe_arithmetic_execution(random_operation,
                                                            random_number1,
                                                            random_number2))

        user_answer = get_user_input(question=question_text)

        # if user's input is not a number then its a wrong answer
        try:
            user_answer = float(user_answer)
            user_answer = apply_rounding(user_answer)
            user_is_right = is_answer_correct(arithmetic_result, user_answer)
        except ValueError:
            user_is_right = False

        if user_is_right:
            print_great_success()
            successful_loops += 1
        else:
            print_fail(wrong_answer=user_answer,
                       correct_answer=arithmetic_result)
            break

    if successful_loops >= NUMBER_OF_SUCCESSFUL_TRIES:
        print_cheers_to(username)


def get_random_operation_sign():
    random_int_number = get_random_number(1, 4)

    if random_int_number == 1:
        return '+'
    elif random_int_number == 2:
        return '-'
    elif random_int_number == 3:
        return '*'
    elif random_int_number == 4:
        return '/'


def safe_arithmetic_execution(operation, *numbers):
    """applies operation to numbers*"""

    accumulator = numbers[0]  # assign to the very first value

    for idx, number in enumerate(numbers):
        if idx > 0:  # skip first iteration
            if it_casts_to_int(number):  # check if param casts to integer
                if operation == '+':
                    accumulator = accumulator + number
                elif operation == '-':
                    accumulator = accumulator - number
                elif operation == '*':
                    accumulator = accumulator * number
                elif operation == '/':
                    try:
                        accumulator = accumulator / number
                        accumulator = apply_rounding(accumulator)
                    except ValueError:
                        return False

    return accumulator


def apply_rounding(number):
    return round(number, 2)


def is_answer_correct(correct_answer, user_answer):
    if str(correct_answer) == str(user_answer):
        return True
    else:
        return False


if __name__ == "__main__":
    play_calc_game()
