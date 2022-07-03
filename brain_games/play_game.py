import prompt
import random
from brain_games.is_even import is_even_number


def play():
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_count = 0
    for _ in range(3):
        random_number = random.randint(1, 30)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = is_even_number(random_number)
        if user_answer != correct_answer:
            return f"{'user_answer'} is wrong answer ;(. Correct answer was {'correct_answer'}.\
            Let's try again, {user_name}!"
            break
        elif user_answer == correct_answer:
            correct_count += 1
            print('Correct!')
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    play()
