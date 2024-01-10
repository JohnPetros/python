# Task 51 - Write a script that reads the first term of an AP (Arithmetic Progression). At the end, displays the first 10 terms of that progression

print("=" * 20)
print("{:^20}".format("10 TERMS OF AN AP"))
print("=" * 20)

firstTerm = int(input("First term: "))
step = int(input("Step: "))

lastTerm = firstTerm + (step * 10)

for term in range(firstTerm, lastTerm, step):
    print(f"{term} -> ", end="")

print("END")
