import platform
import os


def logo():
    """ Prints the Logo """
    print(r'''
     .--------.
    / .------. \
   / /        \ \
   | |        | |
  _| |________| |_
.' |_|        |_| '.    88                        88
'._____ ____ _____.'    88                        88
|     .'____'.     |    88                        88
'.__.'.'    '.'.__.'    88  ,adPPYba,   ,adPPYba, 88   ,d8 
'.__  |      |  __.'    88 a8"     "8a a8"     "" 88 ,a8"  
|   '.'.____.'.'   |    88 8b       d8 8b         8888[   
'.____'.____.'____.'    88 "8a,   ,a8" "8a,   ,aa 88`"Yba, 
'.________________.'    88  `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
    ''')


def logo_small():
    """ Prints a small logo """
    print(r'''
 _            _    
| |          | |   
| | ___   ___| | __
| |/ _ \ / __| |/ /
| | (_) | (__|   < 
|_|\___/ \___|_|\_\
    ''')


def key_symbol():
    """ Adds key icon"""
    if platform.system() == 'Windows':
        return ''
    return u'\U0001F511  '


def clear_screen():
    """ Clears the screen """
    if platform.system() == 'Windows':
        os.system('cls')
        return True
    print('\x1b[1J')
    return True


def erase_db():
    """ Erases the database and resets Master Password """

    from support.menu import get_input
    from support.manage_key import get_key_path
    from support.backend.database import remove_db

    print()
    confirm = get_input("Do you want to permanently delete all your data? (y/n): ", lower=True)
    if confirm is False or confirm != 'y':
        print()
        print("Operation Cancelled!")
        return

    os.remove(get_key_path())
    remove_db()

    print()
    print("Your data has been permanently deleted.")
    print()


