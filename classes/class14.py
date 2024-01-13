# Class 14 - Functions (Part 1)
def showLine():
    print("-" * 30)


def showMessage(message):
    print(message)


def sumNumbers(a, b):
    print(f"A = {a} and B = {b}")
    result = a + b
    print(f"The sum is equal to {result}")


def countNumbers(*numbers):
    for number in numbers:
        print(number)
    print("end")


showLine()
showMessage("Example of message")
showLine()

sumNumbers(5, 7)
sumNumbers(b=4, a=1)

countNumbers(1, 2, 3, 4, 5)
