# task 79 - Write a script in which the user can input several numerical values and register them into a list. If the number is already in the list, it will not be added. At the end, all unique numbers will be displayed in ascending order

numbers = []

while True:
    number = int(input("Enter a number: "))

    if number in numbers:
        print("Duplicated number! I will not add it...")
    else:
        numbers.append(number)
        print("Number added successfully!")

    while True:
        response = input("Do you wanna continue? [Y/N] ").strip().upper()
        if response in ["Y", "N"]:
            break

    if response == "N":
        break

numbers.sort()

print("-=" * 30)
print(f"You entered the numbers {numbers}.")
