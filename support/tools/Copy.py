import pyperclip
import hashlib
import time

clipboard_content = ''


def copy(item, field='username', erase=False):
    """ Copies an item """
    global clipboard_content

    if not erase and (type(item) != str or item == ''):
        print("Nothing to copy!")
        return False

    if not erase:
        print(f"The {field} has been copied to the clipboard.")

    pyperclip.copy(item)
    clipboard_content = get_hash(item)


def is_changed():
    """ Returns True if clipboard has changed """
    if clipboard_content:
        changed = clipboard_content != get_hash(pyperclip.paste())
        return changed


def get_hash(item):
    """ returns the hash of item """
    return hashlib.sha256(item.encode()).hexdigest()


def wait():
    """ Wait 10 seconds and erase the clipboard """
    if not clipboard_content:
        return

    print("Clipboard will be erased in 10 seconds")

    try:
        for i in range(10):
            print('.', end='', flush=True)
            time.sleep(1)
            if is_changed():
                print()
                break
    except KeyboardInterrupt:
        pass

    print()
    print()
    erase()


def erase():
    """ Erases the clipboard """
    global clipboard_content

    if not is_changed():
        copy('', erase=True)

    clipboard_content = ''

