# -*- coding: utf-8 -*-


"""Function gameGcd."""


from brain_games.cli import welcome_user, welcome_user1
from brain_games.functional import (
    finish_game,
    goodanswer,
    question,
    randomnumber,
    wrong_answer,
)


def maingcd():
    """Do something interesting.

    # noqa: DAR101 username

    """
    welcome_user()
    print('Find the greatest common divisor of given numbers.')
    username = welcome_user1()
    good = 0
    while good < 3:
        number1 = randomnumber()
        number2 = randomnumber()
        first = number1
        second = number2
        while first != 0 and second != 0:
            if first > second:
                first %= second
            else:
                second %= first
        gcd = first + second
        answer = question(('{} {}'.format(number1, number2)))
        if answer == str(gcd):
            goodanswer()
            good += 1
        else:
            wrong_answer(username, answer, gcd)
    finish_game(username)
