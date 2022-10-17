import platform
import os
from settings import settings


def get_dir_path():
    """ Returns key path """
    if platform.system() == 'Windows':
        _dir = os.path.expanduser('~') + '\\.lock\\'
    else:
        _dir = os.path.expanduser('~') + '/.lock/'

    return _dir


def get_key_path():
    """ Returns key file path """
    return get_dir_path() + '.secure'


def check_key_file():
    """ Makes key file if not exists """
    key_path = get_key_path()

    try:
        key_file = open(key_path, 'r')
        key_file.close()
        return True

    except FileNotFoundError:
        make_key_file()


def make_key_file():
    """ Make the key file """
    key_path = get_key_path()
    if not os.path.exists(get_dir_path()):
        os.mkdir(get_dir_path())
    key_file = open(key_path, 'w')
    key_file.close()


def write_key():
    """ Write the encrypted key to the file"""
    check_key_file()
    key_path = get_key_path()
    key_file = open(key_path, 'w')
    enc_key = settings['enc_key'].digest_key().hex()
    key_file.write(enc_key)
    key_file.close()
