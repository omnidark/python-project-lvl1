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

def even():
    number = randrange(100)
    game_message = 'Answer "yes" if the number is even, otherwise answer "no".'
    return number, is_even(number), game_message
