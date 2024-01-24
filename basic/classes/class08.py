# Class 08 - While Loop


counter = 5

evenNumbers = oddNumbers = 0

while counter > 0:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1

    counter -= 1


print(f"You entered {evenNumbers} even numbers and {oddNumbers} odd numbers")
