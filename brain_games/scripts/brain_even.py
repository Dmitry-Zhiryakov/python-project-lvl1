#!/usr/bin/env python
from brain_games.engine_games import engine_games
from brain_games.games.even \
    import TASK_DESCRIPTION, get_question_and_correct_answer


def main():
    engine_games(TASK_DESCRIPTION, get_question_and_correct_answer)


if __name__ == '__main__':
    main()
