from .database import make_con, close_con
from .. import menu
from ..settings import settings
from support.tools.generate_passwd import generate_random_passwd
import time


def edit_menu(item):
    """ Edit an item """
    print()
    action = menu.get_input(
        message='What would you like to edit [(n)ame / u(r)l / (u)sername / (p)assword / (b)ack]: ',
        lower=True
    )

    if action == 'n':
        update('name', item)
    elif action == 'r':
        update('url', item)
    elif action == 'u':
        update('username', item)
    elif action == 'p':
        update('password', item)
    elif action == 'b':
        return

    return


def update_rec(id_, field, value, table='Usernames'):
    """ Updates the record in the db """
    con, cur = make_con(db='Password_manager')
    cur.execute(f'UPDATE {table} SET {field} = "{value}" WHERE Item = {id_};')
    con.commit()
    close_con(con)


def update(field, rec):
    """ Updates the table usernames in mysql """
    ref = {'name': 3, 'url': 4, 'username': 5}
    id_ = rec[0][0]

    if field != 'password':
        ref_no = ref[field]
        print(f"Current {field}: {rec[0][ref_no] if rec[0][ref_no] != '' else 'Empty!'}")
        new_val = menu.get_input(f'New {field}: ')

        if new_val is not False:
            update_rec(id_, field, new_val)
        else:
            print()
            print("Cancelled!")
            return False
    else:
        print('Password suggestion:', generate_random_passwd())
        password = menu.get_input("Password: ", secure=True)
        if password is not False:
            password = settings['enc_key'].encrypt(password.encode())
            update_rec(id_, field, password, table='Passwords')
        else:
            print()
            print("Cancelled!")
            return False

    print(f"The {field} has been updated.")
    print()
    time.sleep(2)

    return True

