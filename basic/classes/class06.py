# Class 06 - Nested Condditions

name = input("What's your name? ")

if name == "Gustav":
    print("How beatiaful name")
elif name == "Peter" or name == "Mary" or name == "Paul":
    print("Your name is very popular")
elif name in "Ana Claude Jessica July":
    print("Pretty female name")
else:
    print("Your name is really normal")

print(f"Have a good day, {name}!")
