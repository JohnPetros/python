# task 83 - Write a script that reads the name and weight of several users, storing all of them into a list. At the end, display:
# - The amount of the registered users
# - The list of the heaviest users
# - The list of the lightest users

users = list()
user = list()

heaviest_users = list()
lightest_users = list()

while True:
    user.append(input("Name: "))
    user.append(float(input("Weight: ")))

    users.append(user[:])
    user.clear()

    while True:
        response = input("Do you wanna continue? [Y/N] ").strip().upper()
        if response in ["Y", "N"]:
            break

    if response == "N":
        break

lightest_weight = users[0][1]
heaviest_weight = users[0][1]
heaviest_users.append(users[0][0])
lightest_users.append(users[0][0])

for user in users:
    if user[1] > heaviest_weight:
        if len(heaviest_users) > 0:
            heaviest_users.pop()

        heaviest_weight = user[1]
        heaviest_users.append(user[0])
    elif user[1] == heaviest_weight and user[0] not in heaviest_users:
        heaviest_users.append(user[0])

    if user[1] < lightest_weight:
        if len(heaviest_users) > 0:
            lightest_users.pop()

        lightest_weight = user[1]
        lightest_users.append(user[0])
    elif user[1] == lightest_weight and user[0] not in lightest_users:
        lightest_users.append(user[0])


print(f"In total there are {len(users)} users")
print(f"The heaviest weight is {heaviest_weight:.2f} of: {heaviest_users}")
print(f"The lightest weight is {lightest_weight:.2f} of: {lightest_users}")
