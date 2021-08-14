"""GCD game."""
from math import gcd
from random import randrange

game_message = 'Find the greatest common divisor of given numbers.'


def gcd_game():
    """Return greatest common divisor betwen two random numbers.

    Returns:
        str: Two random numbers
        str: Greatest common divisor betwen two random numbers

    """
    first_number, second_number = randrange(1, 100), randrange(1, 100)
    question = '{0} {1}'.format(first_number, second_number)
    return question, str(gcd(first_number, second_number))
