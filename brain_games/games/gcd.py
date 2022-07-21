import random
from math import gcd


GAME_RULE = 'Find the greatest common divisor of given numbers.'
MINIMUM_VALUE = 3
MAXIMUM_VALUE = 25


def get_random_list(divider):
    random_list = [num for num in range(3, 101) if num % divider == 0]
    return random_list


def task_and_correct_answer():
    divider = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
    random_list = get_random_list(divider)
    random_number1 = random.choice(random_list)
    random_number2 = random.choice(random_list)
    task = f'{random_number1} {random_number2}'
    correct_answer = gcd(random_number1, random_number2)
    return task, correct_answer


if __name__ == '__main__':
    task_and_correct_answer()
