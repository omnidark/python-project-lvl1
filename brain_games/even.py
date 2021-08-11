"""Even game."""
from random import randrange

import prompt


def is_even(number):
    """Return whether a number is even.

    Args:
        number (int): Number to check.

    Returns:
        str: The return value. yes - if number is even, no - if not.

    """
    if number % 2 == 0:
        return 'yes'
    return 'no'


def even_game(user_name):
    """Start the even game.

    Args:
        user_name (str): The name of user.

    Returns:
        bool: The return value. False if user give wrong answer.

    """
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempts_count = 2
    while attempts_count >= 0:
        number = randrange(100)
        print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')
        correct_answer = is_even(number)
        if correct_answer == answer:
            print('Correct!')
            attempts_count -= 1
        else:
            error_message = """'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!'"""
            print(error_message.format(answer, correct_answer, user_name))
            return False
    print('Congratulations, {0}!'.format(user_name))
