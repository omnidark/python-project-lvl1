"""Even game."""
from random import randrange


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

def even_game():
    """Return whether a number is even.

    Args:
        number (int): Number to check.

    Returns:
        str: The return value. yes - if number is even, no - if not.

    """
    game_message = 'Answer "yes" if the number is even, otherwise answer "no".'
    number = randrange(100)
    return number, is_even(number), game_message
