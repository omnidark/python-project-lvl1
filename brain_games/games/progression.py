"""Progression game."""
from random import randrange

game_message = 'What number is missing in the progression?'


def progression_game():
    """Return greatest common divisor betwen two random numbers.

    Returns:
        str: Two random numbers
        str: Greatest common divisor betwen two random numbers

    """
    progression_len = randrange(5, 11)
    progression_step = randrange(2, 11)
    index = 0
    progression = ['']
    progression[index] = randrange(1, 100)
    target_number_index = randrange(0, progression_len)
    while progression_len > index:
        progression.insert(index + 1, progression[index] + progression_step)
        if index == target_number_index:
            target_number = progression[index]
            progression[index] = '..'
        index += 1
    question = ''
    for i in progression:
        question = '{} {}'.format(question, i)
    return question[1:], str(target_number)
