# -*- coding: utf-8 -*-


"""Function Welcome."""


import prompt


def welcome_user():
    """Welcome."""
    print('Welcome to the Brain Games!')


def welcome_user1():
    """Return the value, name.

    # noqa: DAR201

    """
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {}!'.format(name))
    print('')
    return name
