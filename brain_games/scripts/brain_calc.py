#!/usr/bin/env python3
"""brain-calc init script."""
from brain_games.cli import welcome_user
from brain_games.game import attempts_count, start_game
from brain_games.games.calc import calc_game, game_message


def main():
    """brain-calc start the game."""
    user_name = welcome_user()
    start_game(user_name, calc_game, attempts_count, game_message)


if __name__ == '__main__':
    main()
