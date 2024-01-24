# task 85 - Write a script that reads 7 numbers and puts them all in a UNIQUE list, dividing them into even and odd numbers. After that, display the even and odd numbers in asceding order

numbers = [[], []]

for counter in range(0, 7):
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)

numbers[0].sort()
numbers[1].sort()

print("*" * 30)
print(f"The entered even numbers are {numbers[0]}")
print(f"The entered odd numbers are {numbers[1]}")
