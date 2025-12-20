"""
Pure python generator script.

Generates and returns a specified length of password string.
if a length is not specified, returns the default password length
as defined in the global scope of the script module.

Copyright @ 2023 Brian Obot
"""

import os
import sys
from random import choice
from datetime import datetime
from string import ascii_letters, digits, punctuation
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    
    LOGFILE: str = "passwords.log"
    

settings = Settings()


BASE_PATH = os.path.dirname(os.path.abspath(__file__))

DEFAULT_PASSWORD_LENGTH: int = 16
DISABLE_PASSWORD_LOGGING: bool = False
DEFAULT_PASSWORD_LOG_FILE: str = os.path.join(BASE_PATH, settings.LOGFILE)


if len(sys.argv) > 1:
    try:
        arg = int(sys.argv[1])
    except Exception as err:
        print(f"Error: {err}, falling back to length of {DEFAULT_PASSWORD_LENGTH}")
        arg = DEFAULT_PASSWORD_LENGTH
    try:
        DISABLE_PASSWORD_LOGGING = bool(int(sys.argv[2]))
    except Exception as err:
        pass
else:
    arg = DEFAULT_PASSWORD_LENGTH


def generate_password(length: int = DEFAULT_PASSWORD_LENGTH) -> str:
    ALL_CHARS = ascii_letters + digits + punctuation
    password = []
    for _ in range(length):
        password.append(choice(ALL_CHARS))
    return "".join(password)


def log_password_generation(password: str):
    with open(DEFAULT_PASSWORD_LOG_FILE, "a+") as log_file:
        log_file.write(f"[{datetime.now()}]: {password}\n")


def format_display(password: str):
    print(f"Generated Password\n{'-' * len(password)}\n{password}\n{'-' * len(password)}")


if __name__ == "__main__":
    password = generate_password(arg)
    log_password_generation(password) if not DISABLE_PASSWORD_LOGGING else None
    format_display(password)
    
