# WE HAVE TO IMPORT THE RANDOM NUMBER MODULE IN THIS CASE

import random
from turtle import up

print("Hello, what is you name")

userName = input()

print(f"Well {userName}, I am thinking of number between 1 and 10. Can you guess what it is? :")

# THIS GIVES US A RANDOM INTEGER BETWEEN 1 AND 20, INCLUDING 1 AND 20
secretNumber = random.randint(1,10)

# HERE WE ARE LIMITING THE AMOUNT OF TIMES THAT THE USER CAN GUESS 
# THIS INCLUDES 1 BUT NOT 7
for guesses in range(1,7): 

    print("type in your guess:")
    userGuessInput = int(input())

    if userGuessInput == secretNumber: 
        print(f"Correct! The Right number was {secretNumber}")
        break

    elif userGuessInput > secretNumber: 
        print("Incorrect. Your guess was too high")

    elif userGuessInput < secretNumber: 
        print("Incorrect. Your guess was too lowLee")

print(f"you took {str(guesses)} guesses to answer")