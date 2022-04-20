from random import randint, choice


task_description = 'What number is missing in the progression?'
PROGRESSION_LEN = 10


def get_question_and_correct_answer():
    begin_of_progression = randint(1, 20)
    range_progression_step = (2, 3, 5)
    progression_step = choice(range_progression_step)
    progression = ''
    hidden_index = randint(0, 9)
    counter = 0
    while counter < PROGRESSION_LEN:
        progression_item = begin_of_progression + (counter * progression_step)
        item_to_add = ''
        if counter == hidden_index:
            item_to_add = '..'
            correct_answer = progression_item
        else:
            item_to_add = str(progression_item)
        progression = progression + item_to_add + ' '
        counter = counter + 1
    question = progression
    return question, correct_answer
