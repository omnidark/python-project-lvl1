import prompt


def game(user_name, game, attempts_count):
    """Start the even game.

    Args:
        user_name (str): The name of user.

    Returns:
        bool: The return value. False if user give wrong answer.

    """
    print(game()[2])
    while attempts_count > 0:
        game_context = game()
        print('Question: {0}'.format(game_context[0]))
        answer = prompt.string('Your answer: ')
        if game_context[1] == answer:
            print('Correct!')
            attempts_count -= 1
        else:
            error_message = """'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!'"""
            print(error_message.format(answer, game_context[1], user_name))
            return False
    print('Congratulations, {0}!'.format(user_name))