"""Progression game."""
from random import randrange

game_message = 'What number is missing in the progression?'


def get_progression(progression_len, progression_step, progression_start):
    """Return random progression and hide one random number.

    Args:
        progression_len (int): Len of pregression.
        progression_step (int): Step between two numbers in progression.
        progression_start (int): The number at which the progression starts.

    Returns:
        list: The random progression
        int: Hided random number

    """
    index = 0
    progression = ['']
    progression[index] = progression_start
    target_number_index = randrange(0, progression_len)
    while progression_len > index:
        progression.insert(index + 1, progression[index] + progression_step)
        if index == target_number_index:
            target_number = progression[index]
            progression[index] = '..'
        index += 1
    return progression, target_number


def progression_game():
    """Return progression game question and answer.

    Returns:
        str: Question - random pregression with customized params
        str: Hided random number

    """
    progression_limit = 11
    p_len = randrange(5, progression_limit)
    p_step = randrange(2, progression_limit)
    progression = get_progression(p_len, p_step, randrange(1, 100))
    question = ''
    for element in progression[0]:
        question = '{0} {1}'.format(question, element)
    return question[1:], str(progression[1])
