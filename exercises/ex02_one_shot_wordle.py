"""EX02 - One Shot Wordle."""


__author__ = "730617864"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word = "python"                                                          # secret_word is "python" as it is given for the 
users_word: str = input(f"What is your {str(len(secret_word))}-letter guess?")   # We wanted a variable like lenght to be assigned as string as we want the lenght of the secretword to be printed as it changes. 
initialized: int = 0                                                            # It is used as an increment which check the lenght of the secretword.
emoji: str = ""                                                                 # emoji has an empty string because it get changed as we move through the program. 
while len(secret_word) != len(users_word):                                      # CONDITION - WHETHER THE LENGHT OF THE SECRET WORD IS EQUAL TO THAT OF LENGHT OF THE INPUT TAKEN FROM FROM THE USER.
    users_word = input(f"That was not {str(len(secret_word))} letters! Try again: ")   # f-string is used as lenght of the secret word can change over time and thus, in the input also it should get changed.
while initialized < len(secret_word):                                           # CONDITION - WE GO OVER THE INDEXES OF THE INPUT TAKEN FROM TH USER WHICH SHOULD BE LESS THAN THE INDEX OF THE WORD.
    if users_word[initialized] == secret_word[initialized]:                     # We use if-else statement: if - is used to to make the index green which matches the index of the secret word. 
        emoji = emoji + GREEN_BOX                                               
    else:                                                                       # else - is for to get yellow and white boxes in place.
        existing_character: bool = False                                        # existing_character is assigned to be false at first to get yrllow and white boxes in palce.
        alternate_index: int = 0                                                # We introduce alternate_index as an int intialized to 0 to check that the lenght of the input doesn't exceed the lenght of the users_word. 
        while alternate_index < len(secret_word) and existing_character is False:   # CONDITION - Index of the input should not be greater than that of the secre_word and existing_character is assigned False.
            if secret_word[alternate_index] == users_word[initialized]:         # if-else statement: if the letter of the secret_word matches to that of the input then existing_character wherever placed in the word turns False into True.
                existing_character = True                                       
            else:                                                               # else - it is incremented by 1 to over the other letters.
                alternate_index = alternate_index + 1                       
        if existing_character is True:                                          # Then as it goes through the loop, the places where the input's character matches to that of the letter in the secretword is required to get it turned to yellow.
            emoji = emoji + YELLOW_BOX                                          # Otherwise, we want it to get turned it into white box.
        else:
            emoji = emoji + WHITE_BOX
    initialized = initialized + 1
print(emoji)
if secret_word != users_word:                                                   # This if-else statement is placed here due to the fact that if we place it above the while loop. The result of the code would show us the statement and then the boxes.
    print("Not quite. Play again soon!")                                        # Here, we end the code with exclamatory statements which gives feedback to the user.
else:
    print("Woo! You got it!")
        users_word: str = input(f"Enter a {str(expected_lenght)} character word: ")
    while len(users_word) != expected_lenght:
        users_word = input(f"That wasn't {str(expected_lenght)} chars! Try again: ")
    return users_word

users_word: str = input(f"Enter a {expected_lenght} character word: ")
    while len(users_word) != expected_lenght:
        users_word = input(f"That wasn't {expected_lenght} chars! Try again: ")
    return users_word