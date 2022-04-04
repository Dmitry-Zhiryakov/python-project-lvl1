import random


def task():
    return print('Find the greatest common divisor of given numbers.')


def ask_question_and_get_correct_answer():
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    print('Question: {} {}'.format(number_1, number_2))
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    return number_1 + number_2


def calculate_result(correct_answer, user_answer):
    return str(correct_answer) == user_answer
