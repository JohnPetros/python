# Class 14 - Functions (Part 2)

# help(print)


# def square(n=2):
#     """Takes in a number n, returns the square of n"""
#     return n**2


# help(square)

# square()


def calculate_factorial(number=1):
    factorial = 1

    for counter in range(number, 0, -1):
        factorial *= counter

    return factorial


print(calculate_factorial(5))
print(calculate_factorial(4))
print(calculate_factorial())
