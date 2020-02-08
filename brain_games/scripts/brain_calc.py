# -*- coding: utf-8 -*-


"""Function Even."""

from brain_games.cli import welcome_user1
from brain_games.games.calc import game_calc, question


def maincalc():
    """Foo bar documentation."""
    name = welcome_user1()
    game_calc()
    question(name)
    question(name)
    question(name)
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    maincalc()
