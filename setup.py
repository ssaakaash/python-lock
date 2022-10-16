from menu import get_input
from settings import settings
from Encryption import Encryption
import database
from manage_key import write_key


def initialize():
    """ Lock Setup """

    print("Welcome to Lock. Please choose a super secure master password.")
    print()

    while True:
        key = get_key_input()
        if key is False:
            return False

        if key:
            settings['enc_key'] = Encryption(key.encode())
            write_key()

            con, cur = database.make_con()
            database.create_db(cur)
            database.close_con(con)

            print()
            print("The database has been created!")

            return True


def get_key_input():
    """ Asks for the master password """
    key = get_input(
        message='Please enter a master password: ',
        secure=True
    )
    if key is False:
        return False

    repeat = get_input(
        message='Please confirm your master password: ',
        secure=True
    )
    if repeat is False:
        return False

    if check_repeat(key, repeat) and key_is_valid(key):
        return key

    return None


def key_is_valid(key):
    """ Return true if valid key """
    if len(key) < 8:
        print()
        print("Master Password should be at least 8 characters")
        print()
        return False
    return True


def check_repeat(key, repeat):
    """ Check if the password is correctly typed both times """
    if key != repeat:
        print()
        print("The master password does not match the confirmation. Please try again.")
        print()
        return False
    return True
