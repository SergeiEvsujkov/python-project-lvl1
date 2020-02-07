# -*- coding: utf-8 -*-


"""Function Even."""

from brain_games.cli import welcome_user1
from brain_games.games.even import game_even, question


def main():
    """Foo bar documentation."""
    game_even()
    name = welcome_user1()
    question(name)
    question(name)
    question(name)
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
