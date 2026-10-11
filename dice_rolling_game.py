"""
Task 1: Dice Rolling Game
Simulates rolling a pair of dice and asks the user whether to roll again.
"""

import random


def roll_dice():
    """Return a tuple with two random numbers between 1 and 6 (inclusive)."""
    return random.randint(1, 6), random.randint(1, 6)


def main():
    print("=" * 36)
    print("       DICE ROLLING GAME")
    print("=" * 36)

    roll_count = 0

    while True:
        die1, die2 = roll_dice()
        roll_count += 1

        print(f"\nRoll #{roll_count}")
        print(f"  Die 1: {die1}")
        print(f"  Die 2: {die2}")
        print(f"  Total: {die1 + die2}")

        # Keep asking until the user gives a valid answer
        while True:
            choice = input("\nRoll again? (yes/no): ").strip().lower()
            if choice in ("yes", "y", "no", "n"):
                break
            print("Invalid input. Please type 'yes' or 'no'.")

        if choice in ("no", "n"):
            print(f"\nThanks for playing! You rolled {roll_count} time(s).")
            break


if __name__ == "__main__":
    main()