# -*- coding: utf-8 -*-


"""Function Main."""

import prompt

from brain_games.scripts.brain_even import maineven
from brain_games.scripts.brain_calc import maincalc

def main():
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
