# task 100 - Write a script tha contains an empty list and two functions. The first function will draw five numbers to be appended to the list and the second one will display the sum of all even numbers from the list drawn by the previous function.

from random import randint


def sum_even_numbers(numbers):
    result = 0

    for number in numbers:
        if number % 2 == 0:
            result += number

    print(f"Solving the sum of the even numbers from {numbers} is equal to {result}")


def draw_numbers(numbers):
    for counter in range(0, 5):
        random_number = randint(0, 10)
        numbers.append(random_number)

    print(f"Drawing the five numbers {numbers}... READY!")


numbers = list()

draw_numbers(numbers)
sum_even_numbers(numbers)
