
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
    return u'\U0001F511  '


def clear_screen():
    """ Clears the screen """
    print('\x1b[1J')
    return True

