#!/usr/bin/env python3
"""brain-even init script."""
from brain_games.cli import welcome_user
from brain_games.game import game
from brain_games.games.even import even

def main():
    """brain-even start the game."""
    user_name = welcome_user()
    attempts_count = 3
    game(user_name, even, attempts_count)


if __name__ == '__main__':
    main()
