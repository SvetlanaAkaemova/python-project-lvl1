import random
import prompt
from math import gcd


GAME_TASK = 'Find the greatest common divisor of given numbers.'


def game():
    for divider in range(3, 25):
        divider = random.randint(3, 25)
        random_list = [num for num in range(3, 101) if num % divider == 0]
        a = random.choice(random_list)
        b = random.choice(random_list)
        if a % divider != 0 or b % divider != 0:
            continue
        elif a % divider == 0 and b % divider == 0:
            given_numbers = f'{a} {b}'
            print(f'Question: {given_numbers}')
            break
    correct_answer = gcd(a, b)
    user_answer = int(prompt.string('Your answer: '))
    return correct_answer, user_answer


if __name__ == '__main__':
    game()
