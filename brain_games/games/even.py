import random


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MINIMUM_VALUE = 1
MAXIMUM_VALUE = 30


def is_even(number):
    return number % 2 == 0


def task_and_correct_answer():
    task = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
    if is_even(task):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return task, correct_answer


if __name__ == '__main__':
    task_and_correct_answer()
