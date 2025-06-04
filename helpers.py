from string import ascii_lowercase, digits
from random import choice, randrange, shuffle

def create_random_username():
    n = randrange(6, 10)
    return ''.join([choice(ascii_lowercase) for _ in range(n)])

def create_random_email():
    return create_random_username() + '@' + create_random_username() + '.com'

def create_random_password():
    symbols = '!@#$%^&*()'
    password = list(create_random_username() + choice(digits) + choice(symbols) + choice(ascii_lowercase).upper())
    shuffle(password)
    return ''.join(password)

def random_payload():
    return {'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_username()}