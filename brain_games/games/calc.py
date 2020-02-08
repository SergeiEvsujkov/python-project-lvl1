# -*- coding: utf-8 -*-


"""Function gameCalc."""


from brain_games.cli import welcome_user, welcome_user1
from brain_games.functional import (
    finish_game,
    goodanswer,
    question,
    randomnumber,
    randomsymbol,
    wrong_answer,
)


def maincalc():
    """Do something interesting.

    # noqa: DAR101 username

    """
    welcome_user()
    print('What is the result of the expression?')
    username = welcome_user1()
    good = 0
    while good < 3:
        number1 = randomnumber()
        number2 = randomsymbol()
        number3 = randomnumber()
        if number2 == '*':
            number = number1 * number3
        else:
            number = number1 + number3
        answer = question(('{} {} {}'.format(number1, number2, number3)))
        if answer == str(number):
            goodanswer()
            good += 1
        else:
            wrong_answer(username, answer, number)
    finish_game(username)
