import random
import prompt


GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_number(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def game():
    random_number = random.randint(1, 30)
    print(f'Question: {random_number}')
    user_answer = prompt.string('Your answer: ')
    correct_answer = is_even_number(random_number)
    return correct_answer, user_answer


if __name__ == '__main__':
    game()
