# Task 38 - Write a script that reads two integers and compares them displaying a message informing:
# - The first number is larger
# - The second number is larger
# - There is no a larger number, the both are equal

number1 = int(input("First number: "))
number2 = int(input("Second number: "))

if number1 > number2:
    print("The FIRST number is larger")
elif number2 > number1:
    print("The SECOND number is larger")
else:
    print("The both numbers are equal")
