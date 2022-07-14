import random
import prompt


GAME_TASK = 'What is the result of the expression?'


def game():
    a = random.randint(1, 30)
    b = random.randint(1, 10)
    action = [' + ', ' - ', ' * ']
    random_choice = str(a) + random.choice(action) + str(b)
    correct_answer = eval(random_choice)
    print(f'Question: {random_choice}')
    user_answer = int(prompt.string('Your answer: '))
    return correct_answer, user_answer


if __name__ == '__main__':
    game()
