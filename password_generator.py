import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y','z']

caps_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_', '@', '~', '^']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def generator():
    """Generates random password by given sequence of chars."""

    random_lower_letters = [random.choice(letters) for _ in range(random.randint(3, 5))]
    random_upper_letters = [random.choice(caps_letters) for _ in range(random.randint(3, 5))]
    random_symbols = [random.choice(symbols) for _ in range(random.randint(1, 2))]
    random_numbers = [random.choice(numbers) for _ in range(random.randint(1, 2))]

    password_chars = random_lower_letters + random_upper_letters + random_symbols + random_numbers

    randomized_password = password_chars[:]
    random.shuffle(randomized_password)

    return "".join(randomized_password)
