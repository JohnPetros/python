# Task 49 - Remake the task 9 displaying the multiplication table of a number entered by the user, but now using for loop

number = int(input("Enter a number: "))

for multiplicator in range(0, 11):
    print(f"{number} x {multiplicator:2} = {number * multiplicator}")
