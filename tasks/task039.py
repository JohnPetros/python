# Task 39 - Write a script that reads a young man's birth year and informs, based on his age, whether he has not  enlisted in military service, whether it's time to enlist, i.e., he has already exceeded the military enlistment deadline. Your script will also display the remaining time or how much he has exceeded the deadline

from datetime import date

birthYear = int(input("Your birth year: "))

currentYear = date.today().year

age = currentYear - birthYear

print(f"Who was born in {birthYear} is {age} years old in {currentYear}.")

if age < 18:
    print(f"There are {18 - age} years until the military enlistment.")
    print(f"Your military enlistment will be in {birthYear + 18}.")
elif age == 18:
    print("You must enlist IMMEDIATELY!")
else:
    print(f"You should have enlisted {age - 18} years ago.")
