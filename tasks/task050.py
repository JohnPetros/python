# Task 50 - Write a script that reads 6 integers and displays the sum of only those that are even numbers. If the number is odd, disregard it

total = 0

for multiplicator in range(1, 7):
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        total += number

print(f"The sum of the even numbers is equal to {total}")
