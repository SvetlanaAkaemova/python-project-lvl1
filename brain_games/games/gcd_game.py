import random
from math import gcd
from brain_games.games.structure import welcome_to, greeting, \
    NUMBER_OF_ROUNDS, question, answer, wrong_answer, correct, congrats


def gcd_fn():  # noqa: C901
    welcome_to()
    user_name = greeting()
    print('Find the greatest common divisor of given numbers.')
    count = 0
    for _ in range(NUMBER_OF_ROUNDS):
        for divider in range(3, 25):
            divider = random.randint(3, 25)
            random_list = [num for num in range(3, 101) if num % divider == 0]
            a = random.choice(random_list)
            b = random.choice(random_list)
            if a % divider != 0 or b % divider != 0:
                continue
            elif a % divider == 0 and b % divider == 0:
                given_numbers = f' {a} {b}'
                question(given_numbers)
                break
        user_answer = int(answer())
        correct_answer = gcd(a, b)
        if user_answer != correct_answer:
            wrong_answer(user_answer, correct_answer, user_name)
            break
        elif user_answer == correct_answer:
            correct()
            count += 1
    else:
        congrats(user_name)


if __name__ == '__main__':
    gcd_fn()
