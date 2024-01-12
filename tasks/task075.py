# task 75 - Make a script that reads 4 numbers and put them into a tuple. At the end display:
# - The amount of number 9's occurrences
# - The position the number 3 occurs
# - The even numbers

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
number4 = int(input("Enter the fourth number: "))

numbers = (number1, number2, number3, number4)

print(f"You entered the numbers: {numbers}")
print(f"The number 9 appears {numbers.count(9)} times")

if 3 in numbers:
    print(f"The number 3 appears at the {numbers.index(3) + 1} position")
else:
    print("The number 3 does not occurs in any position within the tuple")


print("You entered even numbers were: ", end="")
for number in numbers:
    if number % 2 == 0:
        print(number, end=" ")
