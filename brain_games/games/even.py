# -*- coding: utf-8 -*-


"""Function gameEven."""


from brain_games.cli import welcome_user, welcome_user1
from brain_games.functional import (
    finish_game,
    goodanswer,
    question,
    randomnumber,
    wrong_answer,
)


def maineven():
    """Do something interesting.

    # noqa: DAR101 username

    """
    welcome_user()
    print('Answer "yes" if number even otherwise answer "no".')
    username = welcome_user1()
    good = 0
    while good < 3:
        task = randomnumber()
        answer = question(task)
        if (task % 2 == 0 and answer == 'yes') or (task % 2 == 1 and answer == 'no'):
            goodanswer()
            good += 1
        elif task % 2 == 0:
            wrong_answer(username, answer, 'yes')
        else:
            wrong_answer(username, answer, 'no')
    finish_game(username)
