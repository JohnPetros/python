# task 80 - Write a script in which the user can enter 5 numerical values and register them in a list at the correct position without using sort method. At the end display the sorted list.

numbers = []

for counter in range(0, 5):
    new_number = int(input("Enter a number: "))

    if len(numbers) == 0 or new_number > numbers[-1]:
        numbers.append(new_number)
        print("Added at the final position of the list...")

    for number in numbers:
        if new_number < number:
            new_number_position = numbers.index(number)

            numbers.insert(new_number_position, new_number)
            print(f"Added at the position {new_number_position} of the list...")
            break


print(numbers)
