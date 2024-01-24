# Task 63 - Write a script that reads an integer n and displays the n first terms of a Fibonacci Senquence
# Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

print("-" * 10)
print("Fibonacci Senquence")
print("-" * 10)

values = int(input("How many values do you want to display: "))

firstValue = 0
secondValue = 1

print(firstValue, end=" -> ")
print(secondValue, end=" -> ")

while values > 2:
    nextValue = firstValue + secondValue

    print(nextValue, end=" -> ")

    firstValue = secondValue
    secondValue = nextValue
    values -= 1

print("END")
