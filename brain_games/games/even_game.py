import random


GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_number(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def game():
    random_number = random.randint(1, 30)
    task = random_number
    correct_answer = is_even_number(random_number)
    return task, correct_answer


if __name__ == '__main__':
    game()
