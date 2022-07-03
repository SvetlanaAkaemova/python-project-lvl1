import random


random_number = random.randint(1, 30)


def is_even_number(random_number):
    if random_number % 2 == 0:
        return 'yes'
    else:
        return 'no'
