# -*- coding: utf-8 -*-


"""Function gamePrime."""


from brain_games.cli import welcome_user, welcome_user1
from brain_games.functional import (
    finish_game,
    goodanswer,
    question,
    randomnumber,
    wrong_answer,
)


def mainprime():
    """Do something interesting.

    # noqa: DAR101 username

    """
    welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    username = welcome_user1()
    good = 0
    while good < 3:
        number = randomnumber()
        if number >= 2:
            index = 2
            res = 'yes'
            while index < number:
                if abs(number) % index == 0:
                    res = 'no'
                    index = number
                else:
                    index += 1
        else:
            res = 'no'
        answer = question(number)
        if answer == res:
            goodanswer()
            good += 1
        else:
            wrong_answer(username, answer, res)
    finish_game(username)
