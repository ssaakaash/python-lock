from utils import logo
from manage_key import get_key_path
import setup
import os
from menu import unlock


def initialize():
    """ Initializes the program """
    logo()
    key_path = get_key_path()

    if not os.path.isfile(get_key_path()):
        setup.initialize()

    unlock()


def main():
    initialize()


if __name__ == '__main__':
    main()
