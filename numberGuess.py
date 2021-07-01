#Guess my number between 1 & 100
from random import *
from os import system, name

# Clear screen function
def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Create random # function
def createNum():
    num = randint(1,101)
    return num

#Enter your guess
clearScreen()
number = createNum()
exitGame = False
tries = int(0)
print("Welcome to guess a random number.  \nThe number will be between 1 and 100.")

while(exitGame != True):
    guess = int(input("Please enter your guess: "))
    tries += 1 
    if guess == number:
        print(f"Congrats for guess the number {number}")
        print(f"It took you {tries} to win.")       
        while(True):
            ans = str(input("Do you wish to play again? (Y/N)"))
            if ans == 'y' or ans == 'Y':
                number = createNum()
                clearScreen()
                tries = 0
                break
            elif ans == 'n' or ans == 'N':
                exitGame = True
                break
            else:
                print("Incorrect response.")

    elif guess < number:
        print("Guess to low.")
    
    else:
        print("Guess to high.")

print("Thank you for playing...")
