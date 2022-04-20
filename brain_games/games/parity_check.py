from random import randint


task_description = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_correct_answer():
    random_number = randint(0, 100)
    question = '{}'.format(random_number)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
