import random


GAME_RULE = 'What number is missing in the progression?'
MINIMUM_VALUE = 5
MAXIMUM_VALUE = 12
NUMBER_OF_MEMBERS = 10


def get_progression(a1, d, number_of_members):
    last_member = a1 + d * number_of_members
    progression = list(range(a1, last_member, d))
    return progression


def get_progression_string(progression, hidden_number):
    progression_string = " ".join(map(str, progression))
    task = progression_string.replace(str(hidden_number), '..')
    return task


def task_and_correct_answer():
    first_member = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
    difference = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
    progression = get_progression(first_member, difference, NUMBER_OF_MEMBERS)
    hidden_number = random.choice(progression)
    task = get_progression_string(progression, hidden_number)
    correct_answer = hidden_number
    return task, correct_answer


if __name__ == '__main__':
    task_and_correct_answer()
