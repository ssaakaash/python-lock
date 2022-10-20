import mysql.connector as ms
from tabulate import tabulate
import menu
from utils import clear_screen
import time
from generate_passwd import generate_random_passwd
from settings import settings


def make_con(db=None):
    """ Make a mySQL connection """
    PASS = 'my3ql'
    # PASS = 'Pr#sql654'
    if db:
        con = ms.connect(host='localhost', user='root', passwd=PASS, database=db)
    else:
        con = ms.connect(host='localhost', user='root', passwd=PASS)
    cur = con.cursor()
    return con, cur


def create_db(cur):
    """ Create the Database """
    cur.execute('CREATE DATABASE IF NOT EXISTS Password_manager;')
    cur.execute('USE Password_manager;')
    cur.execute('''CREATE TABLE IF NOT EXISTS Usernames (
        Item int primary key auto_increment,
        Category varchar(30),
        Name varchar(30),
        URL varchar(50),
        Username varchar(30)
    );''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Passwords (
        Item int primary key auto_increment,
        Password varchar(1000)
    );''')


def get_all_rec():
    """ Display all the details """
    con, cur = make_con(db='Password_manager')
    cur.execute('select * from Usernames')
    all_rec = cur.fetchall()
    close_con(con)
    return all_rec


def get_rec_count():
    """ Return the number of records """
    return len(get_all_rec())


def close_con(con):
    """ Close the mySQL connection """
    con.close()


def to_table(rows=[]):
    """ Print the rows as table """
    if len(rows) > 0:
        print()
        print(tabulate(rows, ['Item', 'Category', 'Name', 'URL', 'Username']))
    else:
        print()
        print('No login items added yet. Add some!')
        print()


def query_db(query, table='Usernames'):
    """ Query a specific table in the database """
    con, cur = make_con(db='Password_manager')
    cur.execute(f'select * from {table} where {query};')
    rec = cur.fetchall()
    close_con(con)
    return rec


def search_general(query):
    """ Search by keyword (Name, URL, Username) """
    query = '%' + query + '%'
    recs = query_db(f'Name LIKE "{query}" OR URL LIKE "{query}" OR Username LIKE "{query}"')
    return recs


def search_id(query):
    """ Search database by id if query is int """
    if query.isdigit():
        rec = query_db(f'item = {query}')
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


def show_item(item):
    """ Shows one password item """
    clear_screen()
    to_table(item)
    print()

    while True:
        action = menu.get_input(
            message='Choose an option [sh(o)w password / (e)dit / (d)elete / (b)ack]: ',
            lower=True
        )
        if action is False:
            print()

        if action == 'o':
            # Show the password
            return show_password(item)
        elif action == 'e':
            # Edit the details
            pass
        elif action == 'd':
            # Delete the password
            deleted = delete(item)
            if deleted:
                return True
        elif action in ['s', 'b', 'q']:
            return action


def delete_rec(_id):
    """ Deletes a record given the id """
    con, cur = make_con(db='Password_manager')
    cur.execute(f"DELETE FROM Usernames WHERE Item = {_id};")
    cur.execute(f"DELETE FROM Passwords WHERE Item = {_id};")
    con.commit()
    close_con(con)


def delete(item):
    """ Deletes the entire record """
    confirm = menu.get_input("Confirm deletion? (y/n): ", lower=True)
    if confirm is False or confirm != 'y':
        print()
        print('Operation Cancelled!')
        print()
    else:
        _id = item[0][0]
        delete_rec(_id)
        print()
        print("Successfully deleted the record.")
        print()

        time.sleep(2)
        return True
    return False


def add_items(name, url='', user=''):
    """ Adds a new login item to the db """
    con, cur = make_con(db='Password_manager')
    cur.execute(f"INSERT INTO Usernames (Name, URL, Username) VALUES ('{name}', '{url}', '{user}');")
    con.commit()
    close_con(con)


def add_pass(password=''):
    """ Adds the encrypted password to the db """
    password = settings['enc_key'].encrypt(password.encode())
    con, cur = make_con(db='Password_manager')
    cur.execute(f'INSERT INTO Passwords (Password) VALUES ("{password}");')
    con.commit()
    close_con(con)


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

