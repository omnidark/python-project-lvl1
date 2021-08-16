"""Prime game."""
from random import randrange

game_message = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Return whether a number is prime.

    Args:
        number (int): Number to check.

    Returns:
        str: The return value. yes - if number is prime, no - if not.

    """
    index = 2
    while index < number:
        if number % index == 0:
            return 'no'
        index += 1
    return 'yes'


def prime_game():
    """Return a number and check number to prime.

    Returns:
        int: Number
        str: yes - if number is prime, no - if not.

    """
    numbers_range = 200
    number = randrange(1, numbers_range)
    return number, is_prime(number)
