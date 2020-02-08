# -*- coding: utf-8 -*-


"""Functions All."""


import random

import prompt


def randomnumber():
    """Random number."""
    return random.randint(1, 100)


def randomsymbol():
    """Random symbol."""
    return random.choice(('*', '+'))


def question(task):
    """Print question."""
    print('Question: {}'.format(task))
    return prompt.string('You answer: ')


def wrong_answer(name_user, answer, good_answer):
    """If wrong answer."""
    print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, good_answer))
    print("Let's try again, {}!".format(name_user))


def goodanswer():
    """If good answer."""
    print('Correct!')


def finish_game(username):
    """Finish game."""
    print('Congratulations, {}!'.format(username))
