# Task 58 - Writes a script that reads in which the computer will "think" of a number between 0 and 10. But now the user will try to guess util they get it right, displaying at the end the amount of the attempts needed to win the game.

from random import randint

print("I'm your computer...")

number = randint(0, 10)

print("I just thought of a number between 0 and 10.")
print("Can you guess which number it was?")

guess = int(input("What is your guess? "))

attempts = 0

while guess != number:
    if number > guess:
        print("Larger... Try again.")
    else:
        print("Smaller... Try again.")

    attempts += 1

    guess = int(input("What is your guess? "))


print(f"You got it with {attempts} attempts! Congratulations!")
