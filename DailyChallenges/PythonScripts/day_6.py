# custom_charset.py (Created the file and added the characters listed below )
# characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Task: Generate a random 8-character password 

import random
import math
import custom_charset

def generate_password():
    password = ""
    count = 0
    while count < 8:
        index = math.floor(random.random() * len(custom_charset.characters))
        password += custom_charset.characters[index]
        count += 1
    return password

print("Your Password:", generate_password())
