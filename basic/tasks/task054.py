# Task 54 - Write a script that reads the birth year of 7 users. At the end displays the amount of users who have not yet reached legal age (21) and the amount of users who are already of legal age

from datetime import date

usersOfLegalAge = 0
usersUnderLegalAge = 0

for user in range(1, 8):
    birthYear = int(input(f"What year was the {user}º user born? "))
    age = date.today().year - birthYear

    if age >= 21:
        usersOfLegalAge += 1
    else:
        usersUnderLegalAge += 1

print(f"In the total we had {usersUnderLegalAge} users who are under the legal age")
print(f"In the total we had {usersOfLegalAge} users who are of legal age")
