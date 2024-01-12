# Class 10 - Tuples

snack = ("hamburguer", "juice", "pizza", "pudim")

print(snack)
print(snack[1])
print(snack[-2])
print(snack[1:3])
print(snack[:2])
print(snack[-3:])

# snack[0] = "soda" 🚫

for index in range(0, len(snack)):
    print(f"I'll eat {snack[index]} which is at the {index}º position.")

print("I ate too much!")

for food in snack:
    print(f"I'll eat {food}")

print("I ate too much!")

for index, food in enumerate(snack):
    print(f"I'll eat {food} which is at the {index}º position.")

print("I ate too much!")

print(sorted(snack))

del snack

numbers = (5, 2, 3, 4, 5)

print(numbers.count(5))
print(numbers.index(5))
print(numbers.index(5, 1))
