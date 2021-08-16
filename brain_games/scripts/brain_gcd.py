#!/usr/bin/env python3
"""brain-gcd init script."""
from brain_games.cli import welcome_user
from brain_games.game import start_game
from brain_games.games.gcd import game_message, gcd_game


def main():
    """brain-gcd start the game."""
    user_name = welcome_user()
    attempts_count = 3
    start_game(user_name, gcd_game, attempts_count, game_message)


if __name__ == '__main__':
    main()
