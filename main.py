"""
Pure python generator script.
Generates and returns a specified length of password string.
if a length is not specified, returns the default password length
as defined in the global scope of the script module.

Copyright 2023 Brian Obot
"""

from string import ascii_letters, digits
from random import choice

DEFAULT_PASSWORD_LENGTH = 8

try:
    arg = sys.argv[1]
except:
    arg = DEFAULT_PASSWORD_LENGTH

def generate_password(length=None):
    ALL_CHARS = ascii_letters + digits
    password = []
    for char in range(length):
        password.append(choice(ALL_CHARS))
    return "".join(password)

if __name__ == "__main__":
    password = generate_password(arg)
    print(f"Generated Password = {password}")
