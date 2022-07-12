import random
from brain_games.games.structure import welcome_to, greeting, \
    NUMBER_OF_ROUNDS, question, answer, wrong_answer, correct, congrats


def progression():
    welcome_to()
    user_name = greeting()
    print('What number is missing in the progression?')
    count = 0
    for _ in range(NUMBER_OF_ROUNDS):
        start = random.randint(1, 12)
        step = random.randint(2, 7)
        stop = start + step * 10
        progression_list = list(range(start, stop, step))
        hidden_number = random.choice(progression_list)
        progression_str = " ".join(map(str, progression_list))
        changed_progression = progression_str.replace(str(hidden_number), '..')
        question(changed_progression)
        correct_answer = hidden_number
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
    progression()
                    
