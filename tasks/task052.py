# Task 52 - Write a script that reads a integer and displays only the prime numbers in the range from 1 to entered number


number = int(input("Enter a number: "))

times = 0

for term in range(1, number + 1):
    if number % term == 0:
        print(f"{term} ", end="")
        times += 1

if times == 2:
    print(f"\n{number} IS PRIME")
else:
    print(f"\n{number} IS NOT PRIME")


print(f"{number} was divided by {times} times")
