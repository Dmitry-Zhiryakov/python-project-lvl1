from random import randint
from math import sqrt


def task():
    return print('Answer "yes" if given number is prime. \
        Otherwise answer "no".')


def ask_question_and_get_correct_answer():
    given_number = randint(2, 50)
    counter = 0
    for i in range(2, int(sqrt(given_number) + 1)):
        if given_number % i == 0:
            counter += 1
    print('Question: {}'.format(given_number))
    if counter == 0:
        return 'yes'
    else:
        return 'no'


def calculate_result(correct_answer, user_answer):
    return correct_answer == str(user_answer)
