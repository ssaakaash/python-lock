import sys

from support.tools.utils import logo, erase_db
from support.manage_key import get_key_path
from support import setup
import os
import argparse
from support.menu import unlock


def initialize(erase=False):
    """ Initializes the program """
    logo()
    key_path = get_key_path()

    if erase:
        erase_db()
        sys.exit()
    
    if not os.path.isfile(get_key_path()):
        setup.initialize()

    unlock()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', "--erase_db", help="Erase the database and Reset Master Password", action='store_true')
    args = parser.parse_args()

    initialize(erase=args.erase_db)


if __name__ == '__main__':
    main()
