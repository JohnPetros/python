# task 81 - Write a script will read multiple numbers and put them into a list. After that, display:
# - The amount of numbers entered
# - The list of numbers in descending order
# - If the number corresponding to the lenght of the list is included in the list

numbers = []

while True:
    number = int(input("Enter a number: "))

    numbers.append(number)

    while True:
        response = input("Do you want to continue? (y/n) ").strip().lower()
        if response in "yn":
            break

    if response == "n":
        break


print("-=" * 30)

numbers_amount = len(numbers)
sorted_numbers = numbers.sort(reverse=True)

print(f"You entered {numbers_amount} numbers.")
print(f"The numbers in descending order are {sorted_numbers}.")
print(
    f"The number {numbers_amount}",
    "was found!" if numbers_amount in numbers else "was not found!",
)
