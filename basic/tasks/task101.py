# task 100 -

from datetime import date


def check_mandatory_vote(birth_year):
    age = date.today().year - birth_year

    if age < 16:
        return "Do not vote"
    elif age < 18 or age > 65:
        return "Optional vote"
    else:
        return "Mandatory vote"


print("-" * 30)

birth_year = int(input("What year were you born?: "))

print(check_mandatory_vote(birth_year))
