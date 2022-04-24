from random import randint


TASK_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
BEGIN_RANGE_NUMBER = 0
END_RANGE_NUMBER = 100


def get_question_and_correct_answer():
    random_number = randint(BEGIN_RANGE_NUMBER, END_RANGE_NUMBER)
    question = '{}'.format(random_number)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
