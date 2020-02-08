# -*- coding: utf-8 -*-


"""Function Main."""

import prompt

from brain_games.scripts.brain_calc import maincalc
from brain_games.scripts.brain_even import maineven
from brain_games.scripts.brain_gcd import maingcd


def main():
    """Foo bar documentation."""
    answermain = prompt.string('Сhoose a game ("even" or "calc" or "gcd): ')
    if answermain == 'even':
        maineven()
    elif answermain == 'calc':
        maincalc()
    elif answermain == 'gcd':
        maingcd()
    else:
        print('Wrong game name')
        main()


if __name__ == '__main__':
    main()
