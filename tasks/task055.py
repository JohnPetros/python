# Task 55 - Writes a script that reads the weight of five users. At the end, displays which was the heaviest and lightest weight

heaviestWeight = 0

for user in range(1, 6):
    weight = float(input(f"What is the weight of the {user}º user? "))

    if weight > heaviestWeight:
        heaviestWeight = weight

    if user == 1:
        lightestWeight = weight

    if weight < lightestWeight:
        lightestWeight = weight


print(f"The entered heaviest weight was {heaviestWeight:.2f}Kg")
print(f"The entered lightest weight was {lightestWeight:.2f}Kg")
