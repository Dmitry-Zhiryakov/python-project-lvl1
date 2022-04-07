#!/usr/bin/env python
from brain_games.engine_games import engine_games
from brain_games.games.parity_check \
    import get_task_description, get_correct_answer, calculate_the_result


def main():
    engine_games(get_task_description, get_correct_answer, calculate_the_result)


if __name__ == '__main__':
    main()
