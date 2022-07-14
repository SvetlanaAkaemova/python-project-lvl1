import random
import prompt


GAME_TASK = 'What number is missing in the progression?'


def game():
    start = random.randint(5, 12)
    step = random.randint(2, 7)
    stop = start + step * 10
    progression_list = list(range(start, stop, step))
    hidden_number = random.choice(progression_list)
    progression_str = " ".join(map(str, progression_list))
    changed_progression = progression_str.replace(str(hidden_number), '..')
    print(f'Question: {changed_progression}')
    correct_answer = hidden_number
    user_answer = int(prompt.string('Your answer: '))
    return correct_answer, user_answer


if __name__ == '__main__':
    game()
