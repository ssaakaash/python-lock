import mysql.connector as ms
from support.backend.database import make_con, close_con, query_db
from support.tools.utils import clear_screen
from support import menu
from tabulate import tabulate


def create_cat():
    """Creates the table Category"""
    con, cur = make_con(db='Password_manager')
    cur.execute('create table if not exists Category\
        (Item_No int primary key auto_increment,\
        Category varchar(30));')
    inbuilt_cat()


def add_cat():
    """Adds a category record"""
    con, cur = make_con(db='Password_manager')
    cat_name = menu.get_input(message='Enter Category name:')
    cur.execute(f'insert into Category (Category) values ("{cat_name}");')
    con.commit()
    close_con(con)
    print('Category has been successfully added')


def rename_cat(cat_no, name):
    """"Renames an existing category"""
    con, cur = make_con('Password_manager')
    cur.execute(f'update Category set Category="{name}" where Item_No="{cat_no}"')
    con.commit()
    close_con(con)


def del_cat(cat_to_del):
    """Deletes the selected category from db when category is not there in username table"""
    con, cur = make_con(db='Password_manager')
    cur.execute(f'delete from category where Category="{cat_to_del}";')
    con.commit()
    close_con(con)


def back():
    """Goes back to the main menu"""
    menu.menu()


def inbuilt_cat():
    """Inserts 3 records in category table"""
    con, cur = make_con('Password_manager')
    cur.execute('insert into Category (Category) values (Personal),(Work),(Gaming);')
    con.commit()
    close_con(con)


def show_cat():
    """Displays ll the contet of table Category"""
    con, cur = make_con('Password_manager')
    cur.execute('select * from Category;')
    rec = cur.fetchall()
    print(tabulate(rec, ['Item_no', 'Category_name']))
    close_con(con)


def cat():
    """Runs the entire category function"""
    clear_screen()
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
            con, cur = make_con(db='Password_manager')
            cat_to_del = menu.get_input(message='Enter category name to delete:',lower=True)
            cur.execute(f'select * from Category natural join Usernames where Usernames.Category="{cat_to_del}";')
            rec = cur.fetchall()
            rec_list=check_cat()

            if rec:
                print('Sorry, can\'t delete this category.. records still exist')
            elif cat_to_del in rec_list:
                del_cat(cat_to_del)
                print()
                print('Category deleted successfully')
                print()
            else:
                print('Category does not exist.. Going back')
            close_con(con)

        elif choice == 'b':
            back()


def check_cat():
    query = 'Item_no is not null'
    rec_list = []
    rec_ = query_db(query, table='Category')
    for rec1 in rec_:
        rec_list.append(rec1[1].lower())
    return rec_list
