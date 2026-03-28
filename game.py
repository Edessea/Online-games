import random

secret_number = random.randint(1, 100)
guess = 0
tries = 0

print("--- WELCOME TO THE GUESSING GAME ---")
print("I'm thinking of a number between 1 and 100.")

while guess != secret_number:
    guess = int(input("Take a guess: "))
    tries = tries + 1
    
    if guess < secret_number:
        print("Higher! ↑")
    elif guess > secret_number:
        print("Lower! ↓")
    else:
        print(f"YOU GOT IT! It took you {tries} tries.")