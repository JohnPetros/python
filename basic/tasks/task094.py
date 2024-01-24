# task 94 - Write a script that reads name, gender and age of several users, storing each users' data into a dictionary and all dictionaries into another dictionary. At the end, display:
# A) The amount of registered users
# B) The average of age
# C) The list of the female users
# D) The list of the users over the average age

users = list()

total_age = 0
women = list()

while True:
    user = dict()
    user["name"] = input("Name: ")

    while True:
        gender = input("Gender: [M/F] ").strip().upper()

        if gender in ["M", "F"]:
            user["gender"] = gender
            break

        print("Error. Answer M or F.")

    user["age"] = int(input("Age: "))

    total_age += user["age"]

    if user["gender"] == "F":
        women.append(user["name"])

    users.append(user)

    while True:
        response = input("Do you want to continue? [Y/N] ").strip().upper()

        if response in ["Y", "N"]:
            break

        print("Error. Try again", end="")

    if response == "N":
        break


average_age = total_age / len(users)

print(f"A) In total there are {len(users)} registered.")
print(f"B) The average of age is {average_age}.")
print("C) The women are", end=" ")
for woman in women:
    print(woman, end=" ")

print()
print("D) List of users over the average of age:")

for user in users:
    if user["age"] > average_age:
        print(f"name: {user['name']}; gender: {user['gender']}; age: {user['age']}")
