import random
import prompt


GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return 'no'
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return 'no'
        divider += 1
    return 'yes'


def game():
    random_number = random.randint(1, 37)
    correct_answer = is_prime(random_number)
    print(f'Question: {random_number}')
    user_answer = prompt.string('Your answer: ')
    return correct_answer, user_answer


if __name__ == '__main__':
    game()
