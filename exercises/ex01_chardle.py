"""EX01 - Chardle - A cute step toward wordle."""

__author__ = "730617864"


word_choice: str = input("Enter a 5-character word: ")
if len(word_choice) != 5:
    print("Error: Word must contain 5 characters.")
    exit()
letter_input: str = input("Enter a single character: ")
if len(letter_input) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter_input + " in " + word_choice)
counting: int = 0


if (letter_input == word_choice[0]):
    print(letter_input + " found at index 0.")
    counting = counting + 1
    
if (letter_input == word_choice[1]):
    print(letter_input + " found at index 1.")
    counting = counting + 1

if (letter_input == word_choice[2]):
    print(letter_input + " found at index 2.")
    counting = counting + 1

if (letter_input == word_choice[3]):
    print(letter_input + " found at index 3.")
    counting = counting + 1

if (letter_input == word_choice[4]):
    print(letter_input + " found at index 4.")
    counting = counting + 1


if (counting == 0):
    print("No instances of " + letter_input + " found in " + word_choice)
if (counting == 1):
    print("1 instance of " + letter_input + " found in " + word_choice)
if (counting == 2):
    print("2 instances of " + letter_input + " found in " + word_choice)
if (counting == 3):
    print("3 instances of " + letter_input + " found in " + word_choice)
if (counting == 4):
    print("4 instances of " + letter_input + " found in " + word_choice)
if (counting == 5):
    print("5 instances of " + letter_input + " found in " + word_choice)