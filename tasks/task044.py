# Task 44 - Create a script that calculates the value to be paid for a product considering its normal price and payment conditions

title = " JOHN'S STORE "
print(f"{title:=^24}")

price = float(input("Price of the purchase: $"))

print("PAYMENT METHODS:")
print("[ 1 ] in cash/check")
print("[ 2 ] in cash by credit card")
print("[ 3 ] 2x by credit card")
print("[ 4 ] 3x or more by credit card")

option = int(input("What is the option? "))

if option == 1:
    print("Your purchase will have a discount of 10%")

    finalPrice = price * 0.9
elif option == 2:
    print("Your purchase will have a discount of 5%")

    finalPrice = price * 0.95
elif option == 3:
    finalPrice = price * 0.95

    print(f"Your purchase will be paid in 2x of ${(finalPrice / 2):.2f}")
elif option == 4:
    installments = int(input("How many installments? "))
    finalPrice = price * 1.2

    print(
        f"Your purchase will be paid in {installments}x of ${(finalPrice / installments):.2f} with 20% interest rate"
    )

print(f"Your purchase of ${price:.2f} will cost ${finalPrice:.2f} in the end")
