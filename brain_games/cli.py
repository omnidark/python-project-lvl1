"""Command line interface for brain-games."""
import prompt


def welcome_user():
    """brain-games welcom-cli."""
    print('Welcome to the Brain Games!')
    print('Hello, {0}!'.format(prompt.string('May I have your name? ')))
