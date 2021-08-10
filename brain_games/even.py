"""Even game."""
from random import randrange

import prompt


def is_even(number):
    """Checking a number for evenness."""
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'

def even_game(user_name):
    """Start the even game."""
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempts_count =  2
    while attempts_count >= 0:
        number = randrange(100)
        print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')
        correct_answer = is_even(number)
        if correct_answer == answer:
            print('Correct!')
            attempts_count -= 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!'".format(answer,correct_answer,user_name))
            return False
    print('Congratulations, {0}!'.format(user_name))
