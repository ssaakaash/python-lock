from .database import make_con, close_con, remove_id_from_recs
from .. import menu
import time


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
        update_order(item)
        print()
        print("Successfully deleted the record.")
        print()

        time.sleep(2)
        return True
    return False


def update_order(item):
    """ Updates the order number for all records above given id """
    item = remove_id_from_recs(item)
    _id = item[0][0]
    con, cur = make_con(db='Password_manager')
    cur.execute(f"UPDATE Usernames SET Number = Number - 1 WHERE Number > {_id}")
    con.commit()
    close_con(con)


