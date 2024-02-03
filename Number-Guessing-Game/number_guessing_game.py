import random

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty level: 'easy' or 'hard': ")
number = random.randint(1, 100)

if difficulty == 'hard':
    attempts = 5
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number:")
        guess = int(input("Make a guess: "))
        if guess == number:
            print("Congratulations! You guessed my number!")
            break
        elif guess < number:
            print("Your guess is too low.\nGuess again.")
            attempts -= 1
        elif guess > number:
            print("Your guess is too high.\nGuess again.")
            attempts -= 1
elif difficulty == 'easy':
    attempts = 20
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number:")
        guess = int(input("Make a guess: "))
        if guess == number:
            print("Congratulations! You guessed my number!")
            break
        elif guess < number:
            print("Your guess is too low.\nGuess again.")
            attempts -= 1
        elif guess > number:
            print("Your guess is too high.\nGuess again.")
            attempts -= 1