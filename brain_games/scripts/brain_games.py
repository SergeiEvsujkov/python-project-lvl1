# -*- coding: utf-8 -*-


"""Function Main."""

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_calc import maincalc
from brain_games.scripts.brain_even import maineven


def main():
    """Foo bar documentation."""
    welcome_user()
    answermain = prompt.string('Сhoose a game ("even" or "calc"): ')
    if answermain == 'even':
        maineven()
    elif answermain == 'calc':
        maincalc()
    else:
        print('Wrong game name')
        main()


if __name__ == '__main__':
    main()
