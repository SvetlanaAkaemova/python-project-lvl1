import prompt
from types import ModuleType


WELCOME = 'Welcome to the Brain Games!'
NUMBER_OF_ROUNDS = 3
CORRECT = 'Correct!'


def run_game(game: ModuleType):
    print(WELCOME)
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.GAME_RULE)
    count = 0
    for _ in range(NUMBER_OF_ROUNDS):
        task, correct_answer = game.task_and_correct_answer()
        print(f'Question: {task}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != str(correct_answer):
            print(f"""'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.
Let's try again, {user_name}!""")
            break
        elif user_answer == str(correct_answer):
            print(CORRECT)
            count += 1
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    run_game(game)  # noqa: F821
