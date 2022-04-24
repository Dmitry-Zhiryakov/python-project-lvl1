import prompt


COUNT_OF_ROUNDS = 3


def engine_games(TASK_DESCRIPTION, get_question_and_correct_answer):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(TASK_DESCRIPTION)
    counter = 0
    while counter < COUNT_OF_ROUNDS:
        question, correct_answer = get_question_and_correct_answer()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if str(correct_answer) == user_answer:
            print('Correct!')
            counter += 1
        else:
            print('\'{}\' is wrong answer ;(. \
Correct answer was \'{}\''.format(user_answer, correct_answer))
            print('Let\'s try again, {}!'.format(user_name))
            break
    else:
        print('Congratulations, {}!'.format(user_name))
