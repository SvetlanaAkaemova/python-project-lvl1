import random


GAME_RULE = 'What is the result of the expression?'
MINIMUM_VALUE = 1
MAXIMUM_VALUE = 20


def task_and_correct_answer():
    random_number1 = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
    random_number2 = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
    action = [' + ', ' - ', ' * ']
    task = f'{random_number1}{random.choice(action)}{random_number2}'
    correct_answer = eval(task)
    return task, correct_answer


if __name__ == '__main__':
    task_and_correct_answer()
