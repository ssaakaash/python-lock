from .database import make_con, close_con, get_rec_count
from ..settings import settings
from support.tools.utils import clear_screen
from .. import menu
from support.tools.generate_passwd import generate_random_passwd
import time
from category import check_cat


def add_items(name, cat_='', url='', user=''):
    """ Adds a new login item to the db """
    con, cur = make_con(db='Password_manager')
    number = get_rec_count() + 1
    cur.execute(f"INSERT INTO Usernames (Name, Category, URL, Username, Number) VALUES ('{name}', '{cat_}', '{url}', '{user}', {number});")
    con.commit()
    close_con(con)


def add_pass(password=''):
    """ Adds the encrypted password to the db """
    password = settings['enc_key'].encrypt(password.encode())
    con, cur = make_con(db='Password_manager')
    cur.execute(f'INSERT INTO Passwords (Password) VALUES ("{password}");')
    con.commit()
    close_con(con)


def add():
    """ Ask for login details and add it """
    clear_screen()

    name = menu.get_input("Name: ")
    if name is False:
        return False

    url = menu.get_input("URL: ")
    if url is False:
        return False

    user = menu.get_input("Username: ")
    if user is False:
        return False

    cat_ = menu.get_input('Category: ')
    if cat_ is False:
        return False
    con, cur = make_con(db='Password_manager')
    rec_list = check_cat()
    if cat_.lower() not in rec_list:
        cur.execute(f'insert into Category (Category) values ("{cat_}")')
    con.commit()
    close_con(con)

    print('Password suggestion:', generate_random_passwd())
    password = menu.get_input("Password: ", secure=True)
    if password is False:
        return False

    add_items(name, url, user)
    add_pass(password)

    print()
    print('The new items have been added!')
    print()

    time.sleep(2)
