"""EX03 - STRUCTURED WORDLE."""

__author__ = "730617864"


def contains_char(anylenght: str, single_chr: str) -> bool:
    #defined the two parameters which will return bool i.e. true and false
    """Answers True if the index of the single_chr contians anylenght."""
    assert len(single_chr) == 1
    increment: int = 0
    
    while increment < len(anylenght):
        if anylenght[increment] == single_chr:
            return True
        else:
            increment = increment + 1    
    return False

def emojified(guess: str, secret: str) -> str:
    """Will return the colored boxes to indicate user's correctness."""
    assert len(guess) == len(secret)
    emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    
    initials: int = 0
    while initials < len(secret):
        if guess[initials] == secret[initials]:
            emoji = emoji + GREEN_BOX
        else:
            if contains_char(secret, guess[initials]):
                emoji = emoji + YELLOW_BOX 
            else:
                emoji = emoji + WHITE_BOX 
        initiials = initials + 1
    return emoji

def input_guess(expected_lenght: int) -> str:
    """Used to correct the user with the correct lenght."""
    users_word: str = input(f"Enter a {expected_lenght} character word: ")
    while len(users_word) != expected_lenght:
        users_word = input(f"That wasn't {expected_lenght} chars! Try again: ")
    return users_word    

def main() -> None:
    """This the point from where the code start and the wordle works."""
    secret = "codes"
    turns: int = 1
    condition: bool = True

    while turns <= 6 and condition is True:
        print(f"=== Turn {turns}/6 ===")
        another_guess: str = input_guess(len(secret))
        print(emojified(another_guess, secret))
        if secret == another_guess:
            my_finishing = False
            print(f"You won in {turns}/6 turns")
        else:
            turns = turns = 1

    if turns > 6:
        print("X/6 - Sorry, try again tomorrow!")    

if __name__ == "__main__":
    main()