from random import randint, choice


TASK_DESCRIPTION = 'What is the result of the expression?'
ARITHMETIC_OPERATION = ['+', '-', '*']
BEGIN_RANGE_NUMBER = 0
END_RANGE_NUMBER = 10


def calculate(number_1, operator, number_2):
    if operator == '+':
        return number_1 + number_2
    if operator == '-':
        return number_1 - number_2
    if operator == '*':
        return number_1 * number_2


def get_question_and_correct_answer():
    operator = choice(ARITHMETIC_OPERATION)
    number_1 = randint(BEGIN_RANGE_NUMBER, END_RANGE_NUMBER)
    number_2 = randint(BEGIN_RANGE_NUMBER, END_RANGE_NUMBER)
    question = '{} {} {}'.format(number_1, operator, number_2)
    correct_answer = calculate(number_1, operator, number_2)
    return question, str(correct_answer)
