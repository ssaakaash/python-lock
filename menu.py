import getpass

import category
from utils import key_symbol
import sys
from settings import settings
from Encryption import Encryption
from manage_key import check_key_file, get_key_path
from utils import clear_screen, logo_small
import database


def get_input(message='', secure=False, lower=False):
    """ Simply gets user input """
    try:
        if secure:
            _input = getpass.getpass(key_symbol() + message)
        else:
            _input = input(message)

        if lower:
            _input = _input.lower()
    except:
        return False

    return _input


def unlock(try_=1):
    """ Asks for Master Password """

    key = get_input(message='Please enter the master password: ', secure=True)

    if key is False:
        sys.exit()

    if check_key(key):
        menu()
    else:
        if try_ >= 3:
            print("Too many incorrect attempts. Access denied.")
            print()
            sys.exit()
        else:
            print("Master password is incorrect. Please try again.")
            print()
            unlock(try_=try_+1)


def check_key(key):
    """ Verify the master password """
    settings['enc_key'] = Encryption(key.encode())
    check_key_file()
    key_file = open(get_key_path(), 'r')
    real_key = key_file.read()

    if settings['enc_key'].digest_key().hex() == real_key:
        return True

    return False


def menu(next_act=None):
    """ Displays starting menu """
    while True:
        clear_screen()
        logo_small()

        print(f"{database.get_rec_count()} items are saved securely")
        print()

        if next_act:
            action = next_act
            next_act = None
        else:
            action = get_input(
                message='Choose an option [(d)isplay / (s)earch / (a)dd / (c)ategory / (q)uit]: ',
                lower=True,
            )
            if action is False:
                print()

        if action == 'q':
            sys.exit()
        elif action == 'd':
            database.to_table(database.get_all_rec())
            next_act = database.search()
        elif action == 'a':
            database.add()
        elif action == 's':
            next_act = database.search()
        elif action == 'c':
            category.cat()
