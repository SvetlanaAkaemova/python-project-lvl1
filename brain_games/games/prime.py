import random


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MINIMUM_VALUE = 1
MAXIMUM_VALUE = 50


def is_prime(number):
    if number < 2:
        return False
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider += 1
    return True


def task_and_correct_answer():
    task = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
    if is_prime(task):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return task, correct_answer


if __name__ == '__main__':
    task_and_correct_answer()
