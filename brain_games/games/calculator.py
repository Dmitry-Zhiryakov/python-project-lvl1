from random import randint, choice


def get_task_description():
    return print('What is the result of the expression?')


def get_correct_answer():
    arithmetic_operations = ['+', '-', '*']
    operator = choice(arithmetic_operations)
    number_1 = randint(0, 10)
    number_2 = randint(0, 10)
    print('Question: {} {} {}'.format(number_1, operator, number_2))
    if operator == '+':
        return number_1 + number_2
    if operator == '-':
        return number_1 - number_2
    if operator == '*':
        return number_1 * number_2


def calculate_the_result(correct_answer, user_answer):
    return str(correct_answer) == user_answer
