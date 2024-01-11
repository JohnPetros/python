# Task 62 - Enhance the task 61 asking if the user wants the script to display more terms. The script ends when the user enters the number 0.

print("Generator of AP")
print("-=" * 10)

firstTerm = int(input("First term: "))
step = int(input("Step of AP: "))

counter = 10
terms = 0

canCount = True

while canCount:
    while counter > 0:
        print(f"{firstTerm} -> ", end="")
        firstTerm += step
        counter -= 1
        terms += 1

    print("Pause")

    additionalTerms = int(input("How many additional terms do you want? "))

    if additionalTerms == 0:
        canCount = False
    else:
        counter = additionalTerms

print(f"Progression is finalized with displayed {terms} terms.")
