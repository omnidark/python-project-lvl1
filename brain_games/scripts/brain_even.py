#!/usr/bin/env python3
"""brain-even init script."""
from brain_games.cli import welcome_user
from brain_games.even import even_game


def main():
    """brain-even start the game."""
    user_name = welcome_user()
    even_game(user_name)


if __name__ == '__main__':
    main()
