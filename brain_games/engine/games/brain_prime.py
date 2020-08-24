"""Prime number game"""

from brain_games.engine import main


# game numbers range
MIN_RANDOM = 1
MAX_RANDOM = 100


def show_description():
    print('Answer \"yes\" if given number is prime. '
          'Otherwise answer \"no\".')


def get_question__right_answer():

    # get question
    random_number = main.get_random_number(MIN_RANDOM, MAX_RANDOM)
    question_text = str(random_number)

    # get right answer
    right_answer = get_correct_answer(random_number)

    # return
    result = {'question': question_text,
              'right_answer': right_answer,
              }

    return result


def get_correct_answer(number):

    is_prime_number = is_prime(number)

    if is_prime_number:
        return 'yes'
    else:
        return 'no'


# def is_answer_correct(is_prime_number, user_input):
#
#     if is_prime_number and user_input == 'yes':
#         return True
#     elif not is_prime_number and user_input == 'no':
#         return True
#     else:
#         return False


def is_prime(number):

    number_is_divisible = False

    if number != 1:     # prime number is always greater than 1
        number_is_divisible = not is_divisible(number)
    else:
        number_is_divisible = False  # 1 is a special case

    return number_is_divisible


def is_divisible(number):

    divisibiliy_trigger = False
    for i in range(2, number):
        if (number % i) == 0:
            divisibiliy_trigger = True

    return divisibiliy_trigger
