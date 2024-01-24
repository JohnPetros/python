# Task 6 - A user provides a birth date in the format dd/mm/yyyy. Write a script that calculates the age of the user

from datetime import datetime


def calculate_age(date):
    birth_date = datetime.strptime(date, "%d/%m/%Y")
    current_date = datetime.today()

    age = current_date.year - birth_date.year

    if birth_date.month > current_date.month or birth_date.day > current_date.day:
        age -= 1

    return f"You are {age} years old."


print(calculate_age("16/03/2002"))
