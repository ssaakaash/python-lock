import mysql.connector as ms
from tabulate import tabulate
import menu
from utils import clear_screen
import time
from generate_passwd import generate_random_passwd
import database2


def make_con(db=None):
    """ Make a mySQL connection """
    #PASS = 'my3ql'
    PASS = 'Pr#sql654'
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


def close_con(con):
    """ Close the mySQL connection """
    con.close()


def to_table(rows=[]):
    """ Print the rows as table """
    if len(rows) > 0:
        print()
        print(tabulate(rows, ['Item', 'Category', 'Name', 'URL', 'Username']))
        print()
    else:
        print()
        print('No login items added yet. Add some!')
        print()


def query_db(query):
    """ Query the database """
    con, cur = make_con(db='Password_manager')
    cur.execute(f'select * from Passwords where {query};')
    rec = cur.fetchall()
    close_con(con)
    return rec


def search_id(query):
    """ Search database by id if query is int """
    if query.isdigit():
        rec = query_db(f'id = {query}')
        if rec:
            return [rec]


def search():
    """ Searches the database """
    query = menu.get_input(message='Search: ')

    if query in ['dis', 'a', 'q' , 'del']:
        return query

    results = search_id(query)

    if len(results) == 1:
        show_item(results)


def show_item(item):
    """ Shows one password item """
    clear_screen()
    print(to_table(item))


def add_items(name, url='', user=''):
    """ Adds a new login item """
    con, cur = make_con(db='Password_manager')
    q = f"INSERT INTO Usernames (Name, URL, Username) VALUES ('{name}', '{url}', '{user}');"
    cur.execute(q)
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

    print('Password:')
    choice=input('(g)enerate password / (e)nter password')
    
    if choice=='g':
        password = generate_random_passwd()
    else:
        password = menu.get_input("Password: ", secure=True)
    if password is False:
        return False

    add_items(name, url, user)

    print()
    print('The new items have been added!')
    print()

    time.sleep(5)


def del_rec():
    con, cur = make_con(db='Password_manager')
    cur.execute('select * from Usernames')
    all_rec = cur.fetchall()
    nme=input('Enter name')
    
    for rec in all_rec:
        if rec[2] == nme:
            cur.execute(f'delete from Usernames where Name="{nme}";')
            print('Record successfully deleted')
            con.commit()
            break
    else:
        print('No such record found')


def search():
    para = input('Search according to (N)ame / (URL) / (U)sername:')
    clear_screen()
    if para == 'N':
        database2.search_name()

    elif para == 'URL':
        database2.search_url()

    elif para == 'U':
        database2.search_username()


def update_rec(rec):
    """ Updates the table usernames in mysql """

    col = menu.get_input(message='Enter 1 or more column to be updated [(N)ame / (U)RL / (Us)ername]:')
    con, cur = database.make_con(db='Password_manager')
    if 'N' in col:
        old_name = menu.get_input('Confirm current name to change')
        new_name = menu.get_input('Enter new name')
        if old_name in rec:
            cur.execute(f'update Usernames set Name = "{new_name}" where Name = "{old_name}";')
            con.commit()
            print('Record successfully updated')
        else:
            print("Currently entered name doesn't match records. Try again")
            update_rec(rec)

    if 'U' in col:
        old_url = menu.get_input('Confirm current url to change')
        new_url = menu.get_input('Enter new url')
        if old_url in rec:
            cur.execute(f'update Usernames set URL = "{new_url}" where URL = "{old_url}";')
            con.commit()
            print('Record successfully updated')
        else:
            print("Currently entered url doesn't match records. Try again")
            update_rec(rec)

    if col 'Us' in col:
        old_uname = menu.get_input('Confirm current username to change')
        new_uname = menu.get_input('Enter new username')
        if old_uname in rec:
            cur.execute(f'update Usernames set Username = "{new_uname}" where Username = "{old_uname}";')
            con.commit()
            print('Record successfully updated')
        else:
            print("Currently entered username doesn't match records. Try again")
            update_rec(rec)
