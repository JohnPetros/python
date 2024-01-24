# task 78 - Write a script that reads 5 numerical values and stores them into a list. At the end, display which were the largest and smallest values entered and their respective positions in the list.

numbers = []

largest_number = 0
smallest_number = 0

for position in range(0, 5):
    number = int(input(f"Enter a number for the position {position}: "))

    numbers.append(number)

    if position == 0:
        smallest_number = number

    if number > largest_number:
        largest_number = number

    if number < smallest_number:
        smallest_number = number


print(f"You entered the numbers {numbers}")

print(f"The largest number was {largest_number} at the positions ", end="")
for position, number in enumerate(numbers):
    if number == largest_number:
        print(position, end="... ")

print(f"\nThe smallest number was {smallest_number} at the positions ", end="")
for position, number in enumerate(numbers):
    if number == smallest_number:
        print(position, end="... ")
