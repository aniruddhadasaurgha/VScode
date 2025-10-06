import random
print("Welcome to the Number Guessing Game!")
print("I just chose a number between 1 and 100. What is the number?")
number = random.randint(1, 100)
guess = None
while guess != number:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break
print("Thanks for playing!")