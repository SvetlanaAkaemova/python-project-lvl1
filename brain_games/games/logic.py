import prompt


WELCOME = f"{'Welcome to the Brain Games!'}"
NUMBER_OF_ROUNDS = 3
CORRECT = f"{'Correct!'}"


def greeting():
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def question(task):
    print(f'Question: {task}')


def answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def wrong_answer(UserAnswer, CorrectAnswer, name):
    print(f"'{UserAnswer}' is wrong answer ;(. Correct answer was '{CorrectAnswer}'.\nLet's try again, {name}!")


def congrats(name):
    print(f'Congratulations, {name}!')


def run_game(module):
    print(WELCOME)
    user_name = greeting()
    print(module.GAME_TASK)
    count = 0
    for _ in range(NUMBER_OF_ROUNDS):
        correct_answer, user_answer = module.game()
        if user_answer != correct_answer:
            wrong_answer(user_answer, correct_answer, user_name)
            break
        elif user_answer == correct_answer:
            print(CORRECT)
            count += 1
    else:
        congrats(user_name)


if __name__ == '__main__':
    run_game(module)  # noqa: F821
