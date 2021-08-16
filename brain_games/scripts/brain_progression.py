#!/usr/bin/env python3
"""brain-progression init script."""
from brain_games.cli import welcome_user
from brain_games.game import attempts_count, start_game
from brain_games.games.progression import game_message, progression_game


def main():
    """brain-progression start the game."""
    user_name = welcome_user()
    start_game(user_name, progression_game, attempts_count, game_message)


if __name__ == '__main__':
    main()
