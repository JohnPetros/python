# Task 48 - Write a script that calculates the sum of all odd numbers that are multiples of 3 and are in the range from 1 to 500

total = 0
oddNumbers = 0

for number in range(1, 501, 2):
    if number % 3 == 0:
        oddNumbers += 1
        total += number

print(total)
print(oddNumbers)
