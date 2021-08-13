"""Calc game."""
import operator
from random import randrange

def random_expression():
    expressions = ('-', '+', '*')
    ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
    }
    expression_symbol = expressions[randrange(3)]
    return ops[expression_symbol], expression_symbol 

def calc_game():
    game_message = 'What is the result of the expression?'
    context = random_expression()
    a, b = randrange(100), randrange(100)
    question = '{} {} {}'.format(a, context[1], b)
    return question, str(context[0](a, b)), game_message
