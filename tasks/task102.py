# task 102 - Write a script that contains a funcion that will receive the user's birth year as parameter, returning a literal value informing whether the user has denied, optional or mandatory voting in the elections.

from datetime import date


def check_mandatory_vote(birth_year):
    age = date.today().year - birth_year

    if age < 16:
        return "Do not voting"
    elif age < 18 or age > 65:
        return "Optional voting"
    else:
        return "Mandatory voting"


print("-" * 30)

birth_year = int(input("What year were you born?: "))

print(check_mandatory_vote(birth_year))
