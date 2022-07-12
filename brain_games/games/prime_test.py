import random


number = random.randint(1, 100)
def is_prime(number):
    if number < 2:
        return 'no'
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return 'no'
        divider += 1
    return 'yes'
print(number)
print(is_prime(number))
