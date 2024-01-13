# task 92 - Write a script that reads the name, birth year, ID and stores them (with the calculated age) into a dictionary. If ID is different from 0, the dictionary will also contain their year of registration and salary. Also calculate

from datetime import date

worker = dict()

worker["name"] = input("Name: ")
worker["birth year"] = int(input("Birth year: "))
worker["ID"] = int(input("ID (0 if there is not): "))

if worker["ID"] != 0:
    worker["registration year"] = int(input("Registration year: "))
    worker["salary"] = float(input("Salary: $"))
    worker["retirement"] = worker["registration year"] + 35

print("-=" * 30)

for key, value in worker.items():
    if key == "birth year":
        print(f"- {key} has the value of {date.today().year - value}")
    elif key == "salary":
        print(f"- {key} has the value of {value:.2f}")
    else:
        print(f"- {key} has the value of {value}")
