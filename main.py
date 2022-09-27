from string import ascii_letters, digits, punctuation
from random import choice

DEFAULT_PASSWORD_LENGTH = 30

try:
    arg = sys.argv[1]
except:
    arg = DEFAULT_PASSWORD_LENGTH

def generate_password(arg=None):
    ALL_CHARS = ascii_letters + digits + punctuation
    password = ""
    for char in range(arg):
        password += choice(ALL_CHARS)
    return password

if __name__ == "__main__":
    password = generate_password(arg)
    print(f"Generated Password = {password}")
