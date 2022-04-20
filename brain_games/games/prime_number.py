from random import randint
from math import sqrt


task_description = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def is_prime(given_number):
    counter = 0
    for i in range(2, int(sqrt(given_number) + 1)):
        if given_number % i == 0:
            counter += 1
    return counter == 0


def get_question_and_correct_answer():
    given_number = randint(2, 50)
    question = given_number
    if is_prime(given_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
