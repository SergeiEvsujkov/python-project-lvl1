# -*- coding: utf-8 -*-


"""Function Welcome."""


import prompt


def welcome_user():
    """Return a user's name."""
    print('Welcome to the Brain Games!')
    print('Hello, {}!'.format(prompt.string('\nMay I have your name? ')))
