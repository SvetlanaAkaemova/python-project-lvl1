import random
from brain_games.games.structure import welcome_to, greeting, \
    NUMBER_OF_ROUNDS, question, answer, wrong_answer, correct, congrats


def calc():
    welcome_to()
    user_name = greeting()
    print('What is the result of the expression?')
    count = 0
    for _ in range(NUMBER_OF_ROUNDS):
        a = random.randint(1, 30)
        b = random.randint(1, 10)
        action = [' + ', ' - ', ' * ']
        random_choice = str(a) + random.choice(action) + str(b)
        correct_answer = eval(random_choice)
        question(random_choice)
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
    calc()
