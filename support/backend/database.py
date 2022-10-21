import mysql.connector as ms
from tabulate import tabulate


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
        Number int not null,
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
    rows = remove_id_from_recs(rows)
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


def remove_id_from_recs(recs):
    """ Returns the recs with Item field removed """
    new_recs = []
    for rec in recs:
        rec = rec[1:]
        new_recs.append(rec)
    return new_recs


