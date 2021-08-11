"""Command line interface for brain-games."""
import prompt


def welcome_user():
    """Brain-games welcom-cli.

    Returns:
        str: The return value. The name of user.

    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    return user_name
