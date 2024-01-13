# task 91 - Write a script in which 4 players roll a dice e get random numbers. Store them into a dictionary. At the end put this dictionary in order, considering that the winner got the largest number from the dice.

from random import randint
from time import sleep

player1 = {"name": "player1"}
player2 = {"name": "player2"}
player3 = {"name": "player3"}
player4 = {"name": "player4"}

players = [player1, player2, player3, player4]

playedNumbers = []

for player in players:
    while True:
        number = randint(1, 6)
        if number not in playedNumbers:
            playedNumbers.append(number)
            player["number"] = number
            print(f'Player {player["number"]} played the number {number}')
            sleep(0.5)
            break

playedNumbers.sort(reverse=True)

print("-=" * 30)
print("== RANKIGN OF PLAYERS ==")
for place in range(1, 5):
    player = dict()

    for current_player in players:
        if current_player["number"] == playedNumbers[place - 1]:
            player = current_player

    print(f'{place}º place: {player["name"]} with {player["number"]}.')
