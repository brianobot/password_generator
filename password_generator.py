"""
Pure python generator script.

Generates and returns a specified length of password string.
if a length is not specified, returns the default password length
as defined in the global scope of the script module.

Copyright @ 2023 Brian Obot
"""

import sys

from string import ascii_letters, digits, punctuation
from random import choice


DEFAULT_PASSWORD_LENGTH = 16

if len(sys.argv) > 1:
    try:
        arg = int(sys.argv[1])
    except Exception as err:
        print(f"Error: {err}, falling back to length of {DEFAULT_PASSWORD_LENGTH}")
        arg = DEFAULT_PASSWORD_LENGTH
else:
    arg = DEFAULT_PASSWORD_LENGTH


def generate_password(length: int = None) -> str:
    ALL_CHARS = ascii_letters + digits + punctuation
    password = []
    for _ in range(length):
        password.append(choice(ALL_CHARS))
    return "".join(password)


if __name__ == "__main__":
    password = generate_password(arg)
    print(f"Generated Password : \n{password}")
