"""Start of any brain game."""
import prompt

attempts_count = 3


def start_game(user_name, game, attempts, game_message):
    """Start the even game.

    Args:
        user_name (str): The name of user.
        game (func): The name of game
        attempts (int): Attemts count
        game_message (str): Game message

    Returns:
        bool: Return False if user loose the game.

    """
    print(game_message)
    while attempts > 0:
        game_context = game()
        print('Question: {0}'.format(game_context[0]))
        answer = prompt.string('Your answer: ')
        if game_context[1] == answer:
            print('Correct!')
            attempts -= 1
        else:
            error_message = """'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!'"""
            print(error_message.format(answer, game_context[1], user_name))
            return False
    print('Congratulations, {0}!'.format(user_name))
