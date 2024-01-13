# task 104 - Write a script that contains a funcion that will receive two optional parameters: the name and the amount os scored goals of a football player. The script should be able to calculate display the player's report card, even if one of the data was not provided correctly


def display_player(name="<unknown>", goals=0):
    if not goals.isnumeric():
        goals = 0

    print("=" * 30)
    return f"the player {name} scored {goals} goal(s) in the championship"


name = input("Name: ").strip()
goals = input("Number of goals: ")

print(display_player(name, goals))
