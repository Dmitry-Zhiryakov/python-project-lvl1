#!/usr/bin/env python
from brain_games.engine_games import engine_games
from brain_games.games.calculator \
    import task_description, get_question_and_correct_answer


def main():
    engine_games(task_description, get_question_and_correct_answer)


if __name__ == '__main__':
    main()
