# Task 41 - The National Confederation of Swimming needs a script that reads the birth year of an athlete and shows their rank based on their age:
# - Until 9 years old: BABY
# - Until 14 years old: JUNIOR
# - Until 19 years old: MID
# - Until 24 years old: SENIOR
# - Above 24 years old: MASTER

from datetime import date

birthYear = int(input("Enter your birth year: "))

age = date.today().year - birthYear

print(f"You are {age} years old")

if age <= 9:
    print("Rank: BABY")
elif age <= 14:
    print("Rank: JUNIOR")
elif age <= 19:
    print("Rank: MID")
elif age <= 24:
    print("Rank: SENIOR")
else:
    print("Rank: MASTER")
