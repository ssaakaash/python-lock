import mysql.connector as ms
import database
import utils
import menu
from tabulate import tabulate


def create_cat():
    """Creates the table Category"""
    con, cur = database.make_con(db='Password_manager')
    cur.execute('create table if not exists Category\
        (Item_No int primary key auto_increment,\
        Category varchar(30));')
    inbuilt_cat()


def add_cat():
    """Adds a category record"""
    con, cur = database.make_con(db='Password_manager')
    cat_name = menu.get_input(message='Enter Category name:')
    cur.execute(f'insert into Category (Category) values ("{cat_name}");')
    con.commit()
    database.close_con(con)
    print('Category has been successfully added')


def rename_cat(cat_no, name):
    """"Renames an existing category"""
    con, cur = database.make_con('Password_manager')
    cur.execute(f'update Category set Category="{name}" where Item_No="{cat_no}"')
    con.commit()
    database.close_con(con)


def del_cat(cat_to_del):
    """Deletes the selected category from db when category is not there in username table"""
    con, cur = database.make_con(db='Password_manager')
    cur.execute(f'delete from category where Category="{cat_to_del}";')


def back():
    """Goes back to the main menu"""
    menu.menu()


def inbuilt_cat():
    """Inserts 3 records in category table"""
    con, cur = database.make_con('Password_manager')
    cur.execute('insert into Category (Category) values (Personal),(Work),(Gaming);')
    con.commit()
    database.close_con(con)


def show_cat():
    """Displays ll the contet of table Category"""
    con, cur = database.make_con('Password_manager')
    cur.execute('select * from Category;')
    rec = cur.fetchall()
    print(tabulate(rec, ['Item_no', 'Category-name']))
    database.close_con(con)


def cat():
    """Runs the entire category function"""
    utils.clear_screen()
    while True:
        choice = menu.get_input(message='Choose an option [(a)dd / (r)ename / (d)elete / (b)ack]:', lower=True)

        if choice == 'a':
            show_cat()
            add_cat()

        elif choice == 'r':
            show_cat()
            cat_no = menu.get_input(message='Enter category number to rename:')
            name = menu.get_input(message='Enter new name of category:')
            rename_cat(cat_no, name)

        elif choice == 'd':
            show_cat()
            cat_to_del = menu.get_input(message='Enter category name to delete:')
            query = f'select * from Category natural join Usernames where Usernames.Category="{cat_to_del}";'
            if database.rec_count(database.query_db(query)):
                print('Sorry, can\'t delete this category.. records still exist')
            else:
                del_cat(cat_to_del)

        elif choice == 'b':
            back()
