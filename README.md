# Password Generator

## Description
Pure python password generator.

## Usage
The script has to be used as standalone script with command line arguments or
can be imported or called by another python program/script

Command Line Usage
- `python password_generator.py` # generate a password of with module default length string 
- `python password_generator.py 8` # generate a password of 8-length string 
- `python password_generator.py 64` # generate a password of 64-length string

Used within a Python Program
```
...
from password_generator import generate_password

...
password = generate_password()
password = generate_password(8)
password = generate_password(64)
```

## Maintainer
- [Brian Obot]('https://www.github.com/brianobot/') <brianobot9@gmail.com>
