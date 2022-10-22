import mysql.connector as ms
from tabulate import tabulate

PASS = 'my3ql'
# PASS = 'Pr#sql654'


def make_con(db=None):
    """ Make a mySQL connection """
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
    cur.execute('''create table if not exists Category ( 
        Item_No int primary key auto_increment,
        Number int not null,
        Category varchar(30)
    );''')
    inbuilt_cat()


def remove_db():
    """ Deletes the database """
    con, cur = make_con()
    cur.execute("DROP DATABASE Password_manager;")
    con.commit()
    close_con(con)


def get_all_rec():
    """ Display all the details """
    con, cur = make_con(db='Password_manager')
    cur.execute('SELECT u.Item, u.Number, c.Category, u.Name, u.URL, u.Username FROM '
                'Usernames u LEFT JOIN Category c ON u.Category = c.Item_no;')
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


def inbuilt_cat():
    """Inserts 3 records in category table"""
    con, cur = make_con('Password_manager')
    cur.execute('INSERT INTO Category (Number, Category) VALUES '
                '(1, "Personal"), '
                '(2, "Work"), '
                '(3, "Gaming");')
    con.commit()
    close_con(con)


def query_db(query, table='Usernames', show_cat=False):
    """ Query a specific table in the database """
    con, cur = make_con(db='Password_manager')
    if show_cat and table == 'Usernames':
        cur.execute(f'SELECT u.Item, u.Number, c.Category, u.Name, u.URL, u.Username FROM '
                    f'Usernames u LEFT JOIN Category c ON u.Category = c.Item_no WHERE {query};')
    else:
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


