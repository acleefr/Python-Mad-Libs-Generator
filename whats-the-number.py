#generate a random number, give it to A

import random

def main():
    secret_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    guess = int(input("What is your guess? "))
    while guess != secret_number:
        if guess > secret_number:
            print("Too high!")
        else:
            print("Too low!")
        guess = int(input("What is your guess? "))
    print("You got it!")
    
main()