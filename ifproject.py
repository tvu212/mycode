#! /usr/bin/env python3
import random 

### Asks for an integer between 6 and 8. Returns error if a string is input ###
try:
    answer1 = int(input("what is an integer between 6 and 8?:"))

except:
    print("invalid string input")

if answer1 == 7:
    print("Correct!")

else:
    print("Incorrect!")


### Asks for an integer and rolls n simulated dice using the random library. Returns error if string is input ###
try:
    diceroll = int(input("How many dice do you want to roll?:"))

except:
    print("invalid string input") 


dicelist = [] ##Future list for dice declared outside of while loop

while diceroll != 0:
    dice = random.randint(1,6)                     ## Rolls the dice
    dicelist.append(dice)                          ## Appends current diceroll to the dicelist
    print(f"You rolled a {dice}!")                 ## Prints the current diceroll
    diceroll -= 1                                  ## Decrements the diceroll by 1



