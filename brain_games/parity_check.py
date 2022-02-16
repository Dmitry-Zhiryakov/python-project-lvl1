import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    return user_name


def question(user_name):
    random_number = random.randint(0, 100)
    answer = prompt.string('Question: ' + str(random_number) + '\n' + 'Your answer: ')

    def parity_check(random_number):
        if random_number % 2 == 0:
            return 'yes'
        else:
            return 'no'
    if answer == 'yes' and parity_check(random_number) == 'yes':
        return ('Correct!')
    elif answer == 'no' and parity_check(random_number) == 'no':
        return ('Correct!')
    else:
        answer != 'yes' or 'no'
        print("'" + answer + "'" + " is wrong answer ;(. Correct answer was " + "'" + parity_check(random_number) + "'.")
        print("Let's try again, {}!".format(user_name))


def repeat_the_question(number_of_repetitions, user_name):
    counter = 1
    while counter <= number_of_repetitions and question(user_name) == 'Correct!':
        print('Correct!')
        counter += 1
    if counter > number_of_repetitions:
        print('Congratulations, {}!'.format(user_name))


def parity_check_main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    repeat_the_question(3, name)
