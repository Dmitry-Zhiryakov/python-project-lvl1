from random import randint


TASK_DESCRIPTION = 'Find the greatest common divisor of given numbers.'
BEGIN_RANGE_NUMBER = 0
END_RANGE_NUMBER = 100


def gcd(number_1, number_2):
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    return number_1 + number_2


def get_question_and_correct_answer():
    number_1 = randint(BEGIN_RANGE_NUMBER, END_RANGE_NUMBER)
    number_2 = randint(BEGIN_RANGE_NUMBER, END_RANGE_NUMBER)
    question = '{} {}'.format(number_1, number_2)
    correct_answer = gcd(number_1, number_2)
    return question, str(correct_answer)
