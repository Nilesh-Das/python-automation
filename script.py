#!usr/bin/python3

#Password Generator
import string
from random import choice, randint

characters = string.ascii_letters +string.punctuation +string.digits
password = ''.join(choice(characters) for _ in range(randint(8, 16)))

print(password)