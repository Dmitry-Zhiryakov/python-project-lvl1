from random import randint, choice


TASK_DESCRIPTION = 'What number is missing in the progression?'
MIN_PROGRESSION_START = 1
MAX_PROGRESSION_START = 20
RANGE_PROGRESSION_STEP = (2, 3, 5)
PROGRESSION_LEN = 10
MIN_HIDDEN_INDEX = 0
MAX_HIDDEN_INDEX = 9


def get_question_and_correct_answer():
    progression_start = randint(MIN_PROGRESSION_START, MAX_PROGRESSION_START)
    progression_step = choice(RANGE_PROGRESSION_STEP)
    progression = ''
    hidden_index = randint(MIN_HIDDEN_INDEX, MAX_HIDDEN_INDEX)
    counter = 0
    while counter < PROGRESSION_LEN:
        progression_item = progression_start + (counter * progression_step)
        item_to_add = ''
        if counter == hidden_index:
            item_to_add = '..'
            correct_answer = progression_item
        else:
            item_to_add = str(progression_item)
        progression = progression + item_to_add + ' '
        counter = counter + 1
    question = progression
    return question, str(correct_answer)
