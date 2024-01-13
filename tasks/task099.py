# task 99 - Write a script that contains a function that receives multiple integers as parameters. Your script should analyze all numbers and informs which one is the largest

from time import sleep


def analyse_numbers(*numbers):
    print("-=" * 30)
    print("Analyzing the provided numbers...", end=" ")
    largest_number = 0

    if len(numbers) > 0:
        for index, number in enumerate(numbers):
            if index == 0:
                largest_number = numbers[0]

            if number > largest_number:
                largest_number = number

            sleep(0.5)
            print(number, end=" ", flush=True)

    print()
    print(f"{len(numbers)} numbers were provided in total")
    print(f"The largest number is {largest_number}")
    print("-=" * 30)


analyse_numbers(2, 9, 7, 1)
analyse_numbers(7, 0)
analyse_numbers(6)
analyse_numbers()
