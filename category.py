import time

from support.backend.database import make_con, close_con, query_db, remove_id_from_recs
from support.tools.utils import clear_screen
from support import menu
from tabulate import tabulate


def get_all_cat():
    """ Returns all the categories from the db """
    con, cur = make_con('Password_manager')
    cur.execute('select * from Category;')
    rec = cur.fetchall()
    return rec


def get_number_of_cats():
    """ Returns the number of categories """
    return len(get_all_cat())


def add_cat():
    """Adds a category record"""
    number = get_number_of_cats() + 1
    con, cur = make_con(db='Password_manager')
    cat_name = menu.get_input(message='Enter Category name: ')
    if not cat_name:
        return False
    cur.execute(f'insert into Category (Number, Category) values ({number}, "{cat_name}");')
    con.commit()
    close_con(con)
    print()
    print('Category has been successfully added')

    time.sleep(2)

    return True


def rename_cat(cat_no, name):
    """"Renames an existing category"""
    con, cur = make_con('Password_manager')
    cur.execute(f'update Category set Category="{name}" where Number="{cat_no}"')
    con.commit()
    close_con(con)


def del_cat(cat_to_del):
    """Deletes the selected category from db when category is not there in username table"""
    con, cur = make_con(db='Password_manager')
    cur.execute(f'delete from category where Number="{cat_to_del}";')
    con.commit()
    close_con(con)


def inbuilt_cat():
    """Inserts 3 records in category table"""
    con, cur = make_con('Password_manager')
    cur.execute('insert into Category (Category) values ("Personal"), ("Work"), ("Gaming");')
    con.commit()
    close_con(con)


def to_table(rows=[]):
    rows = remove_id_from_recs(rows)
    """ Print the rows as table """
    if len(rows) > 0:
        print()
        print(tabulate(rows, ['Item', 'Category']))
    else:
        print()
        print('No categories added yet. Add some!')
        print()


def show_cat():
    """Displays all the content of table Category"""
    recs = get_all_cat()
    to_table(recs)
    print()


def exists(id_):
    """ Check if id exists """
    all_cat = get_all_cat()
    there = False
    for rec in all_cat:
        if rec[1] == id_:
            there = True
    if there:
        return True
    return False


def select(message='Select a category: ', optional=False):
    """ Asks user to choose a category """
    all_cats = get_all_cat()

    if len(all_cats) == 0:
        print()
        print("You did not create a category yet. Please create one.")
        return False

    show_cat()

    id_ = menu.get_input(message)

    try:
        id_int = int(id_)
        if id_int and exists(id_int):
            return id_int
    except ValueError:
        pass

    if optional and id_ == '':
        return None

    print()
    print("Invalid Category!")
    time.sleep(2)

    return False


def rename():
    """ Rename a category """
    id_ = select()

    if not id_:
        return False

    name = menu.get_input("New name: ")
    if not name:
        return False

    rename_cat(id_, name)

    print()
    print("The category has been renamed.")
    time.sleep(2)

    return True


def update_order(_id):
    """ Updates the order number for all records above given id """
    con, cur = make_con(db='Password_manager')
    cur.execute(f"UPDATE Category SET Number = Number - 1 WHERE Number > {_id}")
    con.commit()
    close_con(con)


def delete():
    """ Delete a category """
    id_ = select()
    if not id_:
        return False

    if is_used(id_):
        print()
        print('Sorry, can\'t delete this category.. records still exist')
        return False

    confirm = menu.get_input("Confirm deletion (y/n): ")
    if confirm is False or confirm != 'y':
        print()
        print("Operation Cancelled!")
        return False

    del_cat(id_)
    update_order(id_)
    print()
    print('Category deleted successfully')
    time.sleep(2)

    return True


def is_used(id_):
    """ Check if category is being used """
    con, cur = make_con(db='Password_manager')
    cur.execute(f'select * from Usernames where Category="{id_}";')
    recs = cur.fetchall()
    if recs:
        return True
    return False


def cat():
    """Runs the entire category function"""
    while True:
        clear_screen()
        show_cat()

        choice = menu.get_input(message='Choose an option [(a)dd / (r)ename / (d)elete / (b)ack]: ', lower=True)

        if choice is False:
            print()

        if choice == 'a':
            add_cat()
            return
        elif choice == 'r':
            rename()
            return
        elif choice == 'd':
            delete()
            return
        elif choice == 'b':
            return
