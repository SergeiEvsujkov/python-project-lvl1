import sys
import os
sys.path.append(os.getcwd() + '/brain_games')

#import sys
#sys.path.append('/home/sergei/python-project-lvl1/brain_games')

from cli import welcome_user

def main():
    """Foo bar documentation."""
    welcome_user()


if __name__ == '__main__':
    main()
