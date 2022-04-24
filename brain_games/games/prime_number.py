from random import randint
from math import sqrt


TASK_DESCRIPTION = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'
FIRST_PRIME_NUMBER = 2
LIMIT_RANGE_NUMBER = 50


def is_prime(given_number):
    counter = 0
    for i in range(FIRST_PRIME_NUMBER, int(sqrt(given_number) + 1)):
        if given_number % i == 0:
            counter += 1
    return counter == 0


def get_question_and_correct_answer():
    given_number = randint(FIRST_PRIME_NUMBER, LIMIT_RANGE_NUMBER)
    question = given_number
    if is_prime(given_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
