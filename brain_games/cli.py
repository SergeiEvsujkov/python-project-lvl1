# This Python file uses the following encoding: utf-8
import prompt

def welcome_user() -> str:
    """Do name and return a list."""
    print('Welcome to the Brain Games!')
    print('')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
