# -*- coding: utf-8 -*-


"""Function Main."""

import prompt

from brain_games.scripts.brain_calc import maincalc
from brain_games.scripts.brain_even import maineven
from brain_games.scripts.brain_gcd import maingcd
from brain_games.scripts.brain_progression import mainprogression
from brain_games.scripts.brain_prime import mainprime


def main():
    """Foo bar documentation."""
    answermain = prompt.string('Сhoose a game ("even" or "calc" or "gcd" or "progression" or "prime"): ')
    if answermain == 'even':
        maineven()
    elif answermain == 'calc':
        maincalc()
    elif answermain == 'gcd':
        maingcd()
    elif answermain == 'progression':
        mainprogression()
    elif answermain == 'prime':
        mainprime()
    else:
        print('Wrong game name')
        main()


if __name__ == '__main__':
    main()
