# task 70 - Write a script that reads the name and price of several products. The script should ask if the user want to continue. At the end display:
# The total paid
# The amount of products over $1000.00
# The cheapest product's name

print("=" * 30)
print("{:^30}".format("THE SUPER CHEAP STORE"))
print("=" * 30)

total = 0
productsOver1000 = 0
cheapestProductPrice = 0
cheapestProductName = ""

counter = 1

while True:
    name = input("Product's name: ")
    price = int(input("Product's price: $"))

    if counter == 1:
        cheapestProductPrice = price
        cheapestProductName = name

    counter += 1

    if price < cheapestProductPrice:
        cheapestProductPrice = price
        cheapestProductName = name

    total += price

    if price > 1000:
        productsOver1000 += 1

    while True:
        response = input("Do you want to continue? [Y/N]: ").strip().upper()
        if response not in ["Y", "N"]:
            print("Ivalid response! Please, enter Y (yes) or N (no).")
        else:
            break

    if response == "N":
        break

print("{:=^30}".format("END OF THE SCRIPT"))
print(f"The purchase's total was ${total:.2f}")
print(f"The are {productsOver1000} products over $1000.00")
print(
    f"The cheapest product was {cheapestProductName} that costs ${cheapestProductPrice:.2f}"
)
