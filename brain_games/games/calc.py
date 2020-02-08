# -*- coding: utf-8 -*-


"""Function gameCalc."""


import random

import prompt


def game_calc():
    """Welcome."""
    print('What is the result of the expression?')


def question(username):
    """Do something interesting.

    Args:
        username: The argument.

    # noqa: DAR101 username

    """
    number1 = random.randint(1, 100)
    number2 = random.choice(('*', '+'))
    number3 = random.randint(1, 100)
    if number2 == '*':
        number = number1 * number3
    else:
        number = number1 + number3
    print('Question: {} {} {}'.format(number1, number2, number3))
    answer = prompt.string('You answer: ')
    if answer == str(number):
        print('Correct!')
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, number))
        print("Let's try again, {}!".format(username))
        question(username)
