"""Command line input module."""

import prompt


#############################################

def ask(question):
    user_answer = prompt.string(question)
    return user_answer

#############################################


# def welcome_user():
#     """Ask to input name and greet user."""
#     username = ask_for_username()
#     print('Hello,', username)
#     return username
#
#
# # TODO: 2 eradicate
# def ask_for_username():
#     name = prompt.string('May I have your name? ')
#     return name
#
#
# # TODO: 3 eradicate
# def ask_for_user_input():
#     """User input"""
#     user_answer = prompt.string('Your answer: ')
#     return user_answer
