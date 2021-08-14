#!/usr/bin/env python3
"""brain-even init script."""
from brain_games.cli import welcome_user
from brain_games.game import start_game
from brain_games.games.calc import calc_game, game_message


def main():
    """brain-even start the game."""
    user_name = welcome_user()
    attempts_count = 3
    start_game(user_name, calc_game, attempts_count, game_message)


if __name__ == '__main__':
    main()
