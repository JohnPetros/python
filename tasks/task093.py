# task 93 - Write a script that manages the usage of a football player. The script will read the name, number of matches and goals scored in each match. At the end all these will be stored in a dictionary, including the total of goals scored in a championship

player = dict()


player["name"] = input("Name: ")
matches = int(input(f'How many matches {player["name"]} played? '))

player["goals"] = list()

for match in range(1, matches + 1):
    goals = int(input(f"How many goals in the {match}º match? "))
    player["goals"].append(goals)

player["total"] = sum(player["goals"])

print("=" * 50)
print(player)
print("=" * 50)

for field, value in player.items():
    print(f"The field {field} has the value of {value}")

print("=" * 50)

print(f"The player {player['name']} played for {matches} matches.")

for match in range(1, matches + 1):
    print(
        f"     => In the match {match}, he scored {player['goals'][match - 1]} goals."
    )

print(f'It was {player["total"]} goals in total.')
