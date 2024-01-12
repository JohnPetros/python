# task 76 - Write a script that contains a unique tuple with products' names and their respective prices, in sequence. At the end display a list of these products, arranging them in the form of a table

lines = 60

print("-" * lines)
print("{:^60}".format("TABLE OF PRODUCTS"))
print("-" * lines)

items = (
    "Pen",
    1.75,
    "Eraser",
    2,
    "Notebook",
    15.9,
    "Pencil case",
    25,
    "Protractor",
    4.2,
    "Compass",
    9.99,
    "Backpack",
    120.32,
    "Book",
    34.9,
)


priceCharacters = 7

for item in items:
    if isinstance(item, str):
        dots = lines - len(item) - 1 - priceCharacters
        print("{}".format(item), end="")
        print("." * dots, end="")
    else:
        print("${:7.2f}".format(item))


print("-" * lines)
