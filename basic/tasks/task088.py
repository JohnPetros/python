# task 88 - Write a script that helps a lottery player to make guesses. The script will ask for the amount of games to be generated and draw 6 numbers between 1 to 60 for each game. Registering all of them into a nested list.

from random import randint
from time import sleep

print("-" * 30)
print("{:^30}".format("LOTTERY GAME"))
print("-" * 30)

games_amount = int(input("How many games do you want me to draw? "))

print("-=-=-= {:^10} =-=-=- ".format(f"DRAWING {games_amount} GAMES"))

for counter in range(1, games_amount + 1):
    game = []

    while True:
        number = randint(0, 60)

        if number not in game:
            game.append(number)

        if len(game) == 6:
            break

    game.sort()
    print(f"Game {counter}: {game}")
    sleep(1)

print("-=-=-= {:^7} =-=-=-=- ".format("< GOOD LUCK >"))
