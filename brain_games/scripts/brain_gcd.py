#!/usr/bin/env python
from brain_games.engine import engine_games
from brain_games.games.gcd import task, ask_question_and_get_correct_answer, calculate_result


def main():
    engine_games(task, ask_question_and_get_correct_answer, calculate_result)


if __name__ == '__main__':
    main()
