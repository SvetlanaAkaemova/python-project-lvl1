import random
from brain_games.games import


def even_funktion():
    welcome_to()
    user_name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_count = 0
    for _ in range(3):
        random_number = random.randint(1, 30)
        print(f'Question: {random_number}')
        user_answer = answer()
        correct_answer = is_even_number(random_number)
        if user_answer != correct_answer:
            
            break
        elif user_answer == correct_answer:
            correct_count += 1
            
    else:
        


if __name__ == '__main__':
    even_funktion()
