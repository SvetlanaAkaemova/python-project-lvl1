import random


GAME_TASK = 'What is the result of the expression?'


def game():
    a = random.randint(1, 30)
    b = random.randint(1, 10)
    action = [' + ', ' - ', ' * ']
    random_choice = str(a) + random.choice(action) + str(b)
    task = random_choice
    correct_answer = eval(random_choice)
    return task, correct_answer


if __name__ == '__main__':
    game()
