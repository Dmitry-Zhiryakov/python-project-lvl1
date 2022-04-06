import prompt


def engine_games(get_task_description, game_logic, calculate_result):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    get_task_description()
    counter = 0
    while counter < 3:
        correct_answer = game_logic()
        user_answer = prompt.string('Your answer: ')
        result = calculate_result(correct_answer, user_answer)
        if result is True:
            print('Correct!')
            counter += 1
        else:
            print('\'{}\' is wrong answer ;(. Correct answer was \'{}\''.format(user_answer, correct_answer))
            print('Let\'s try again, {}'.format(user_name))
            break
    if counter == 3:
        print('Congratulations, {}!'.format(user_name))
