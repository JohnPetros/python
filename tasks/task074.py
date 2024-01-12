# task 74 - Write a script that will draw 4 numbers and put them in a tuple. After that display these numbers and also inform the largest and smallest number that are in this tuple.

from random import randint

drawnNumbers = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

largestNumber = drawnNumbers[0]
smallestNumber = drawnNumbers[-1]

for number in drawnNumbers:
    if number > largestNumber:
        largestNumber = number

    if number < smallestNumber:
        smallestNumber = number

print("The drawn numbers were:", end="")
for number in drawnNumbers:
    print(f" {number}", end="")


print(f"\nThe largest number was {largestNumber}.")
print(f"The smallest number was {smallestNumber}.")
