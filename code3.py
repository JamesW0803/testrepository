import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

while True:
    guess = input("Take a guess: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed it in {attempts} tries.")
        break
