from random import randint, choice


def get_task_description():
    return print('What number is missing in the progression?')


def get_correct_answer():
    begin_of_progression = randint(1, 20)
    range_progression_step = (2, 3, 5)
    progression_step = choice(range_progression_step)
    progression = ''
    hidden_value = 0
    hidden_index = randint(0, 9)
    counter = 0
    while counter < 10:
        progression_item = begin_of_progression + (counter * progression_step)
        item_to_add = ''
        if counter == hidden_index:
            item_to_add = '..'
            hidden_value = progression_item
        else:
            item_to_add = str(progression_item)
        progression = progression + item_to_add + ' '
        counter = counter + 1
    print('Question: {}'.format(progression))
    return hidden_value


def calculate_the_result(correct_answer, user_answer):
    return str(correct_answer) == user_answer
