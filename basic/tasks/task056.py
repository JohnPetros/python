# Task 56 - Writes a s

totalAge = 0

olderManAge = 0
olderManName = ""

womenOlder20 = 0

for user in range(1, 5):
    print(f"---- {user}º USER ----")
    name = input("Name: ").strip()
    age = int(input("Age: "))
    gender = input("Gender [M/F]: ").strip().upper()

    if age > olderManAge and gender == "M":
        olderManName = name
        olderManAge = age

    if age > 20 and gender == "F":
        womenOlder20 += 1

    totalAge += age


print(f"The medium of the group is equal to {totalAge / 4}")
print(f"The older man is {olderManAge} and is called {olderManName}")
print(f"In the total there there are {womenOlder20} who are older than 20 years")
