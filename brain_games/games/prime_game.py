import random
from brain_games.games.structure import welcome_to, greeting, NUMBER_OF_ROUNDS,\
    is_prime, question, answer, wrong_answer, correct, congrats


def prime_fn():
    welcome_to()
    user_name = greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    for _ in range(NUMBER_OF_ROUNDS):
        random_number = random.randint(1, 37)
        correct_answer = is_prime(random_number)
        question(random_number)
        user_answer = answer()
        if user_answer != correct_answer:
            wrong_answer(user_answer, correct_answer, user_name)
            break
        elif user_answer == correct_answer:
            correct()
            count += 1
    else:
        congrats(user_name)


if __name__ == '__main__':
    prime_fn()
