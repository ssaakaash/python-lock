import mysql.connector as ms
from tabulate import tabulate
import menu
import database
from utils import clear_screen


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
            option = input('Choose an option [(e)dit / (del)ete / (s)how password / (g)o back]:')
            if option == 'del':
                database.del_rec()
            elif option == 'e':
                update_rec(rec)
            elif option == 's':
                show_passwd()
            elif option == 'g':
                go_back()
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
            option = input('Choose an option [(e)dit / (del)ete / (s)how password / (g)o back]:')
            if option == 'del':
                database.del_rec()
            elif option == 'e':
                update_rec(rec)
            elif option == 's':
                show_passwd()
            elif option == 'g':
                go_back()
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
            option = input('Choose an option [(e)dit / (del)ete / (s)how password / (g)o back]:')
            if option == 'del':
                database.del_rec()
            elif option == 'e':
                update_rec(rec)
            elif option == 's':
                show_passwd()
            elif option == 'g':
                go_back()

            break
    else:
        print('No such record found')


def update_rec(rec):
    '''Updates the table usernames in mysql'''

    col = input('Enter column to be updated [(N)ame , (U)RL , (Us)ername]:')
    con, cur = database.make_con(db='Password_manager')
    if col == 'N':
        old_name = input('Enter current name')
        new_name = input('Enter new name')
        if old_name in rec:
            cur.execute(f'update Usernames set Name = "{new_name}" where Name = "{old_name}";')
            con.commit()
            print('Record successfully updated')
        else:
            print('Currently entered name doesn\'t match records. Try again')
            update_rec(rec)

    elif col == 'U':
        old_url = input('Enter current url')
        new_url = input('Enter new url')
        if old_url in rec:
            cur.execute(f'update Usernames set URL = "{new_url}" where URL = "{old_url}";')
            con.commit()
            print('Record successfully updated')
        else:
            print('Currently entered url doesn\'t match records. Try again')
            update_rec(rec)

    elif col == 'Us':
        old_uname = input('Enter current username')
        new_uname = input('Enter new username')
        if old_uname in rec:
            cur.execute(f'update Usernames set Username = "{new_uname}" where Username = "{old_uname}";')
            con.commit()
            print('Record successfully updated')
        else:
            print('Currently entered username doesn\'t match records. Try again')
            update_rec(rec)


def go_back():
    menu.menu(next_act=None)

