import prompt


def engine_games(get_task_description, get_correct_answer, calculate_result):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    get_task_description()
    count_of_rounds = 3
    counter = 0
    while counter < count_of_rounds:
        correct_answer = get_correct_answer()
        user_answer = prompt.string('Your answer: ')
        result = calculate_result(correct_answer, user_answer)
        if result is True:
            print('Correct!')
            counter += 1
        else:
            print('\'{}\' is wrong answer ;(. \
Correct answer was \'{}\''.format(user_answer, correct_answer))
            print('Let\'s try again, {}'.format(user_name))
            break
    if counter == count_of_rounds:
        print('Congratulations, {}!'.format(user_name))
