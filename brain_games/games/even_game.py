import random
from brain_games.games.structure import welcome_to, greeting, NUMBER_OF_ROUNDS,\
    is_even_number, question, answer, wrong_answer, correct, congrats


def even():
    welcome_to()
    user_name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_count = 0
    for _ in range(NUMBER_OF_ROUNDS):
        random_number = random.randint(1, 30)
        question(random_number)
        user_answer = answer()
        correct_answer = is_even_number(random_number)
        if user_answer != correct_answer:
            wrong_answer(user_answer, correct_answer, user_name)
            break
        elif user_answer == correct_answer:
            correct()
            correct_count += 1
    else:
        congrats(user_name)


if __name__ == '__main__':
    even()
