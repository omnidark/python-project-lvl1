"""Calc game."""
import operator
from random import randrange

game_message = 'What is the result of the expression?'


def random_expression():
    """Return random expression.

    Returns:
        func: Operation of random expression

    """
    expressions = ('-', '+', '*')
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    expression_symbol = expressions[randrange(3)]
    return ops[expression_symbol], expression_symbol


def calc_game():
    """Return calc game context.

    Returns:
        str: Return a question with a random calculation
        str: Return the correct answer to a random calculation

    """
    context = random_expression()
    first_number, second_number = randrange(100), randrange(100)
    question = '{0} {1} {2}'.format(first_number, context[1], second_number)
    return question, str(context[0](first_number, second_number))
