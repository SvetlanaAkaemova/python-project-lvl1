import random
from math import gcd


GAME_RULE = 'Find the greatest common divisor of given numbers.'
FIRST = 3
SECOND = 25


def task_and_correct_answer():
    divider = random.randint(FIRST, SECOND)
    random_list = [num for num in range(3, 101) if num % divider == 0]
    random_number1 = random.choice(random_list)
    random_number2 = random.choice(random_list)
    task = f'{random_number1} {random_number2}'
    correct_answer = gcd(random_number1, random_number2)
    return task, correct_answer


if __name__ == '__main__':
    task_and_correct_answer()
