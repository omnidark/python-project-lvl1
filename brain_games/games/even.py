"""Even game."""
from random import randrange

game_message = 'Answer "yes" if the number is even, otherwise answer "no".'


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
    """Return a number and check number to even.

    Returns:
        int: Number
        str: yes - if number is even, no - if not.

    """
    number = randrange(100)
    return number, is_even(number)
