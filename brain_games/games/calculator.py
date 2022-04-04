import random


def task():
    return print('What is the result of the expression?')


def ask_question_and_get_correct_answer():
    arithmetic_operations = ['+', '-', '*']
    operator = random.choice(arithmetic_operations)
    number_1 = random.randint(0, 10)
    number_2 = random.randint(0, 10)
    print('Question: {} {} {}'.format(number_1, operator, number_2))
    if operator == '+':
        return number_1 + number_2
    if operator == '-':
        return number_1 - number_2
    if operator == '*':
        return number_1 * number_2


def calculate_result(correct_answer, user_answer):
    return str(correct_answer) == user_answer
