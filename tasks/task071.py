# task 71 - Write a script that

from math import trunc

print("=" * 30)
print("{:^30}".format("John's Bank"))
print("=" * 30)

money = int(input("How much do you wanna withdraw? $"))

hundreds = money // 100 * 100
tens = money // 10 % 10 * 10
units = int(str(money)[-1])

if hundreds != 0:
    print(f"Total of fifty dollars cell: {trunc(hundreds / 50)}")

if tens != 0:
    print(f"Total of twenty dollars cells: {trunc(tens / 20)}")

if tens % 20 != 0:
    print(f"Total of ten dollars cells: {trunc((tens % 20) / 10)}")

if units != 0:
    print(f"Total of one dollar cells: {trunc(units)}")

print("=" * 30)
