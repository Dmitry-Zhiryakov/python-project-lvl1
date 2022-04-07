from random import randint


def get_task_description():
    return print('Answer "yes" if the number is even, otherwise answer "no".')


def get_correct_answer():
    random_number = randint(0, 100)
    print('Question: {}'.format(random_number))
    if random_number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def calculate_the_result(correct_answer, user_answer):
    return correct_answer == str(user_answer)
