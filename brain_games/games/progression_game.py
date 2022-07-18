import random


GAME_TASK = 'What number is missing in the progression?'


def game():
    start = random.randint(5, 12)
    step = random.randint(2, 7)
    stop = start + step * 10
    progression_list = list(range(start, stop, step))
    hidden_number = random.choice(progression_list)
    progression_str = " ".join(map(str, progression_list))
    changed_progression = progression_str.replace(str(hidden_number), '..')
    task = changed_progression
    correct_answer = hidden_number
    return task, correct_answer


if __name__ == '__main__':
    game()
