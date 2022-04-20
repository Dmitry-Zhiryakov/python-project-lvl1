from random import randint, choice


task_description = 'What is the result of the expression?'
ARITHMETIC_OPERATION = ['+', '-', '*']


def calculate(number_1, operator, number_2):
    if operator == '+':
        return number_1 + number_2
    if operator == '-':
        return number_1 - number_2
    if operator == '*':
        return number_1 * number_2


def get_question_and_correct_answer():
    operator = choice(ARITHMETIC_OPERATION)
    number_1 = randint(0, 10)
    number_2 = randint(0, 10)
    question = '{} {} {}'.format(number_1, operator, number_2)
    correct_answer = calculate(number_1, operator, number_2)
    return question, correct_answer
