# Class 14 - Functions (Part 1)
def show_line():
    print("-" * 30)


def show_message(message):
    print(message)


def sum_numbers(a, b):
    print(f"A = {a} and B = {b}")
    result = a + b
    print(f"The sum is equal to {result}")


def count_numbers(*numbers):
    for number in numbers:
        print(number)
    print("end")


show_line()
show_message("Example of message")
show_line()

sum_numbers(5, 7)
sum_numbers(b=4, a=1)

count_numbers(1, 2, 3, 4, 5)
