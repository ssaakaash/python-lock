from .. import menu
from .database import query_db, to_table
from ..settings import settings
from ..tools.utils import clear_screen
from . import edit, delete
from ..tools import copy
import time


def show_item(item):
    """ Shows one password item """
    clear_screen()
    to_table(item)
    print()

    while True:
        action = menu.get_input(
            message='Choose an option [copy (u)sername, (p)assword / sh(o)w password / '
                    '(e)dit / (d)elete / (s)earch / (b)ack]: ',
            lower=True
        )
        if action is False:
            print()

        if action == 'u':
            copy.copy(item[0][5], 'username')
            copy.wait()
        elif action == 'p':
            copy.copy(get_password(item[0][0]), 'password')
            copy.wait()
        elif action == 'o':
            # Show the password
            return show_password(item)
        elif action == 'e':
            # Edit the details
            edit.edit_menu(item)
        elif action == 'd':
            # Delete the password
            deleted = delete.delete(item)
            if deleted:
                return True
        elif action in ['s', 'b', 'q']:
            return action


def search_general(query):
    """ Search by keyword (Name, URL, Username) """
    query = '%' + query + '%'
    recs = query_db(f'c.Category LIKE "{query}" OR Name LIKE "{query}" OR '
                    f'URL LIKE "{query}" OR Username LIKE "{query}"',
                    show_cat=True)
    return recs


def search_id(query):
    """ Search database by id if query is int """
    if query.isdigit():
        rec = query_db(f'u.Number = {query}', show_cat=True)
        if rec:
            return rec
    return search_general(query)


def search_results(recs):
    """ Displays the search results """
    to_table(recs)
    print()

    rec_id = menu.get_input('Select an Item # or type any key to go back: ')
    if rec_id:
        try:
            rec = [row for row in recs if row[0] == int(rec_id)]
            if rec:
                return show_item(rec)
        except:
            return False


def search():
    """ Searches the database """
    print()
    query = menu.get_input(message='Search: ')

    if query is False:
        return False

    if query in ['d', 'a', 'q', 's']:
        return query

    results = search_id(query)

    if len(results) == 1:
        show_item(results)
    elif len(results) > 1:
        return search_results(results)
    else:
        try:
            print('No results!')
            time.sleep(2)
        except:
            pass

        return False


def get_password(_id):
    """ Returns the password associated with the id """
    rec = query_db(f'Item = {_id}', 'Passwords')
    cipher = rec[0][1][2:-1]
    password = settings['enc_key'].decrypt(cipher.encode())
    return str(password)[2:-1]


def show_password(item):
    """ Shows the password for 5 seconds """
    _id = item[0][0]
    try:
        print('The password will be hidden after 5 seconds.')
        print('The password is:', get_password(_id))
        time.sleep(5)
    except KeyboardInterrupt:
        pass

    return show_item(item)
