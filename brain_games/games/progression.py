# -*- coding: utf-8 -*-


"""Function gameProgression."""


import random

from brain_games.cli import welcome_user, welcome_user1
from brain_games.functional import (
    finish_game,
    goodanswer,
    question,
    randomnumber,
    wrong_answer,
)


def mainprogression():
    """Do something interesting.

    # noqa: DAR101 username

    """
    welcome_user()
    print('What number is missing in the progression?')
    username = welcome_user1()
    good = 0
    while good < 3:
        startprog = randomnumber()
        stepprog = random.randint(1, 10)
        stopprog = startprog + stepprog * 10
        prog = (list(range(startprog, stopprog, stepprog)))
        index = random.randint(0, 9)
        minusnumber = prog[index]
        prog[index] = '..'
        number = 0
        prog1 = ''
        while number < 10:
            prog1 = '{} {} '.format(prog1, str(prog[number]))
            number += 1
        answer = question(('{}'.format(prog1)))
        if answer == str(minusnumber):
            goodanswer()
            good += 1
        else:
            wrong_answer(username, answer, minusnumber)
    finish_game(username)
