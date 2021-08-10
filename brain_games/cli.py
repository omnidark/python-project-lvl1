"""Command line interface for brain-games."""
import prompt


def welcome_user():
    """brain-games welcom-cli."""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    return user_name


