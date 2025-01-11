#Password Generator

import random
import string

def generate_passweord(length, use_uppercase, use_numbers, use_special_chars):
    characters =string.ascii_lowercase
    if use_uppercase:
        characters +=string.ascii_uppercase
    if use_numbers:
        characters +=string.digits
    if use_special_chars:
        characters +=string.punctuation

    password =''.join(random.choice(characters) for  i in range(length))
    return password

length = int(input("Enter the password length:"))
use_uppercase =input("Include uppercase letters?(yes/no):").lower() =="yes"
use_numbers =input("Include numbers?(yes/no):").lower() =="yes"
use_special_chars =input("Include special characters?(yes/no):").lower() =="yes"

print("Password = ", generate_passweord (length ,use_uppercase ,use_numbers, use_special_chars))