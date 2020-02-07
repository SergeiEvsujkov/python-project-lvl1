# -*- coding: utf-8 -*-


"""Function gameEven."""


import random

import prompt


def game_even():
    """Welcome."""
    print('Welcome to the Brain Games!\nAnswer "yes" if number even otherwise answer "no".')


def question(username):
    """Do something interesting.

    Args:
        username: The argument.

    # noqa: DAR101 username

    """
    number = random.randint(1, 100)
    print('Question: {}'.format(number))
    answer = prompt.string('You answer: ')
    if (number % 2 == 0 and answer == 'yes') or (number % 2 == 1 and answer == 'no'):
        print('Correct!')
    elif number % 2 == 0:
        noanswer = 'yes'
        print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, noanswer))
        print("Let's try again, {}!".format(username))
        question(username)
    elif number % 2 == 1:
        noanswer = 'no'
        print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, noanswer))
        print("Let's try again, {}!".format(username))
        question(username)
