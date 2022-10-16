import mysql.connector as ms


def make_con():
    """ Make a mySQL connection """
    PASS = 'my3ql'
    # PASS = 'my3qlP@ssword'
    con = ms.connect(host='localhost', user='root', passwd=PASS)
    cur = con.cursor()
    return con, cur


def create_db(cur):
    """ Create the Database """
    cur.execute('CREATE DATABASE IF NOT EXISTS Password_manager;')
    cur.execute('USE Password_manager;')
    cur.execute('''CREATE TABLE IF NOT EXISTS Passwords (
        Item int primary key auto_increment,
        Category varchar(30),
        Name varchar(30),
        URL varchar(50),
        Username varchar(30),
        Password varchar(30)
    );''')


def insert_data(con, cur):
    """ Insert data """
    uid = int(input('Enter ID:'))
    uname = input('Enter Username:')
    pwd = input('Enter password:')
    cat = input('Enter category:')
    cur.execute('insert into Details values (%s,%s,%s,%s)', (uid, uname, pwd, cat))
    con.commit()


def delete_rec(con, cur):
    """ Delete a record"""
    uid = int(input('Enter ID of account whose details are to be deleted:'))
    cur.execute('delete from Details where ID=%s', (uid,))
    con.commit()


def display_all_rec(con, cur):
    """ Display all the details """
    cur.execute('select * from Details')
    all_rec = cur.fetchall()
    for rec in all_rec:
        print(rec)


def close_con(con):
    """ Close the mySQL connection """
    con.close()
