# from database import *
import string
import random

chars=string.ascii_letters + string.punctuation + string.digits


def generate_random_passwd():
    passwd=''
    for i in range(10):
        passwd+=random.choice(chars)
    return passwd
    
