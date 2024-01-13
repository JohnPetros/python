# task 95 - Enhance the task 93 so that it works with multiple players, including a system for viewing the usage of each player.

players = list()

while True:
    player = dict()

    player["name"] = input("The name of a player: ")
    matches = int(input(f'How many matches {player["name"]} played? '))

    player["goals"] = list()

    for match in range(1, matches + 1):
        goals = int(input(f"How many goals in the {match}º match? "))
        player["goals"].append(goals)

    player["total"] = sum(player["goals"])

    players.append(player)

    while True:
        response = input("Do you want to continue? [Y/N] ").strip().upper()
        if response in ["Y", "N"]:
            break
        print("Error. Answer Y or N", end=" ")

    if response == "N":
        break


print("-=" * 50)

print(f'{"code":<5}{"name":<15}{"goals":<15}{"total"}')

print("-" * 50)
for code, player in enumerate(players):
    print(
        f'{code:>5} {player["name"]:<15}{str(player["goals"]):<15}{str(player["total"])}'
    )
print("-" * 50)

while True:
    code = int(
        input("From which player do you want to display the data? [999 to stop] ")
    )

    if code == 999:
        break

    if code > len(players) - 1:
        print(f"Player not found with the code {code}. Try again.")
    else:
        player = players[code]

        print(f'Displaying the data of {player["name"]}:')

        for match, goals in enumerate(player["goals"]):
            print(f"In the match {match + 1} scored {goals} goals.")

print("<< Thank your busniness >>")
