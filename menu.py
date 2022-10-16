import getpass
from utils import key_symbol
import sys
from settings import settings
from Encryption import Encryption
from manage_key import check_key_file, get_key_path
from utils import clear_screen, logo_small


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


def unlock():
    """ Asks for Master Password """

    key = get_input(message='Please enter the master password: ', secure=True)

    if key is False:
        sys.exit()

    if check_key(key):
        menu()


def check_key(key):
    """ Verify the master password """
    settings['enc_key'] = Encryption(key.encode())
    check_key_file()
    key_file = open(get_key_path(), 'r')
    real_key = key_file.read()

    if settings['enc_key'].digest_key().hex() == real_key:
        return True

    return False


def menu():
    """ Displays starting menu """
    while True:
        clear_screen()
        logo_small()

        command = get_input(
            message='Choose an option [(d)isplay / (a)dd / (q)uit]: ',
            lower=True,
        )
        if command is False:
            print()

        if command == 'q':
            sys.exit()

