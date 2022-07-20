import random


GAME_RULE = 'What number is missing in the progression?'
FIRST = 5
SECOND = 12


def get_progression_list(a, n, d):
    progression_list = list(range(a, n, d))
    return progression_list


def get_progression_string(progression_list):
    progression_string = " ".join(map(str, progression_list))
    return progression_string


def task_and_correct_answer():
    a = random.randint(FIRST, SECOND)
    d = random.randint(FIRST, SECOND)
    n = a + d * 10
    progression_list = get_progression_list(a, n, d)
    hidden_number = random.choice(progression_list)
    progression_string = get_progression_string(progression_list)
    task = progression_string.replace(str(hidden_number), '..')
    correct_answer = hidden_number
    return task, correct_answer


if __name__ == '__main__':
    task_and_correct_answer()
