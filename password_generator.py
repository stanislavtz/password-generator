import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y','z']

caps_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_', '@', '~', '^']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def insert_random(number, chars_collection, password_chars):
    """Inserts random number of chars in password collection."""
    for i in range(number):
        password_chars.append(random.choice(chars_collection))


def generator():
    """Generates random password by given sequence of chars."""
    password_chars = []

    insert_random(4, letters, password_chars)
    insert_random(4, caps_letters, password_chars)
    insert_random(2, symbols, password_chars)
    insert_random(2, numbers, password_chars)

    randomized_password = password_chars[:]
    random.shuffle(randomized_password)

    return "".join(randomized_password)
