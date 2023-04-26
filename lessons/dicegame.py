"""Randomly rolls dice and sums total."""
from random import randint

roll1: int = randint(1,6)                   # variable: varaible_type = function()
roll2: int = randint(1,6)
roll3: int = randint(1,6)

dice_rolls: list[int] = [roll1,roll2,roll3] #<listname>: list[type of list] = [item1, item2,...]
                                            # Since, we want to sum up the value. So we need 
dice_idx: int = 0                           # Initialization for the while is required.
dice_sum: int = 0
while dice_idx <= len(dice_rolls) - 1:      # Since, lenght is always going ton be one more that's why  we subtract one.
    print(dice_rolls[dice_idx])
    dice_sum += dice_rolls[dice_idx]
    dice_idx += 1                           # Notice, that increment is always written after printing the statement.
print(dice_sum)