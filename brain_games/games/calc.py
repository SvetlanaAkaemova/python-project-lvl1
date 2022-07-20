import random


GAME_RULE = 'What is the result of the expression?'
FIRST = 1
SECOND = 20


def task_and_correct_answer():
    random_number1 = random.randint(FIRST, SECOND)
    random_number2 = random.randint(FIRST, SECOND)
    action = [' + ', ' - ', ' * ']
    task = str(random_number1) + random.choice(action) + str(random_number2)
    correct_answer = eval(task)
    return task, correct_answer


if __name__ == '__main__':
    task_and_correct_answer()
