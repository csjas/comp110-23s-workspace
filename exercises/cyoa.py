"""Choose Your Own Adventure."""

__author__ = "730617864"

import random

points: int = 0
player: str = ""


def greet() -> None:                                            # greeting procedure.
    """Greeting the player."""
    global player
    print("Welcome to the Coinflip guessing game!")
    player = input("What's your name?\n")


def coinflip(players_guess: str) -> int:                                    # coinflip function.
    """Introduction to coin flip game."""
    global points
    player_flips_coin: str = random.choice(['heads', 'tails'])
    print(f"The coin lands on {player_flips_coin}!")
    if players_guess == player_flips_coin:
        points += 1
        print(f"Congratulations, {player}! Your guess was correct and you have scored 1 point.")
    else:
        print(f"Sorry, {player}, better luck next time!")
    return points


def main() -> None:                                                     # main function.
    """Game loop introduction."""
    global player
    global points
    greet()
    print(f"Hello, {player}! Let's play the coinflip guessing game.")
    game: bool = True
    while game:
        print(f"Your current score is {points}.")
        player_guess = input("Enter your guess (heads or tails) or type 'quit' to end the game.\n")
        if player_guess.lower() == "quit":
            print(f"Thank you for playing the game, {player}! Your score is {points}.")
            game = False
        elif player_guess.lower() not in ['heads', 'tails']:
            print("Invalid option, please enter either 'heads' or 'tails'.")
        else:
            coinflip(player_guess.lower())


if __name__ == "__main__":
    main()
