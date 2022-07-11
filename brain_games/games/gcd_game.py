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
        for divisor in range(3, 25):
            divisor = random.randint(3, 25)
            data = [y for y in range(3, 101) if y % divisor == 0]
            a = random.choice(data)
            b = random.choice(data)
            if a % divisor != 0 or b % divisor != 0:
                continue
            elif a % divisor == 0 and b % divisor == 0:
                given_numbers = f' {a} {b}'
                question(given_numbers)
                break
        user_answer = answer()
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
