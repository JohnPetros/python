# Task 61 - Remake the task 51 reading the first term of an AP displaying the first 10 terms of the progress using the While Loop

print("Generator of AP")
print("-=" * 10)

firstTerm = int(input("First term: "))
step = int(input("Step of AP: "))

counter = 10

while counter > 0:
    print(f"{firstTerm} -> ", end="")
    firstTerm += step
    counter -= 1

print("END")
