# Task 60 - Write a script that reads any number and displays its factorial

number = int(input("Enter a number to calulate its factorial: "))

print(f"Calculating factorial of {number} = ", end="")

factorial = number

while number > 1:
    print(f"{number} x ", end="")
    number -= 1
    factorial *= number

print(f"1 = {factorial}")
