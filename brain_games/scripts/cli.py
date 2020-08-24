"""Command line input module."""


import prompt


def ask(question):
    user_answer = prompt.string(question)
    return user_answer
