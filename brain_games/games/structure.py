import prompt


def welcome_to():
    print('Welcome to the Brain Games!')


def greeting():
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


NUMBER_OF_ROUNDS = 3


def question(task):
    print(f'Question: {task}')


def answer():
    UserAnswer = int(prompt.string('Your answer: '))
    return UserAnswer


def wrong_answer(UserAnswer, CorrectAnswer, name):
    print(f"'{UserAnswer}' is wrong answer ;(. Correct answer was '{CorrectAnswer}'.\
    Let's try again, {name}!")


def correct():
    print('Correct!')


def congrats(name):
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    welcome_to()
    greeting()
    user_name  # noqa: F821
    question(task)  # noqa: F821
    answer()
    wrong_answer(UserAnswer, CorrectAnswer, name)  # noqa: F821
    correct()
    congrats(name)  # noqa: F821
