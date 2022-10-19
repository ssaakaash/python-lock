import mysql.connector as ms
from tabulate import tabulate
import menu
import database


def search_name():
    con, cur = database.make_con(db='Password_manager')
    cur.execute('select * from Usernames')
    all_rec = cur.fetchall()
    nme=input('Enter name')
    
    for rec in all_rec:
        if rec[2] == nme:
            cur.execute(f'select * from Usernames where Name="{nme}";')
            rec1=[rec]
            print(tabulate(rec1, headers = ['Item', 'Category', 'Name', 'URL', 'Username']))
            break
    else:
        print('No such record found')


def search_url():
    con, cur = database.make_con(db='Password_manager')
    cur.execute('select * from Usernames')
    all_rec = cur.fetchall()
    url=input('Enter URL')
    
    for rec in all_rec:
        if rec[3] == url:
            print(rec)
            cur.execute(f'select * from Usernames where URL="{url}";')
            rec1=[rec]
            print(tabulate(rec1, headers = ['Item', 'Category', 'Name', 'URL', 'Username']))
            break
    else:
        print('No such record found')


def search_username():
    con, cur = database.make_con(db='Password_manager')
    cur.execute('select * from Usernames')
    all_rec = cur.fetchall()
    uname=input('Enter Username')
    
    for rec in all_rec:
        if rec[4] == uname:
            cur.execute(f'select * from Usernames where Username="{uname}";')
            rec1=[rec]
            print(tabulate(rec1, headers = ['Item', 'Category', 'Name', 'URL', 'Username']))
            break
    else:
        print('No such record found')



# def update_rec()





