# Task 36 - Write a script to approve a bank loan for buying a house. Ask for the house price, the buyer's salary, and the number of years they plan to pay it off.
# The monthly installment cannot exceed 30% of the salary otherwise the installement will be declined

price = float(input("The house's price: "))
salary = float(input("The Buyer's salary: "))
years = int(input("The finance's years: "))

installment = price / (years * 12)

print(
    f"To pay a house for ${price:.2f} in {years} the installment will be ${installment:.2f}"
)

if installment > (salary * 0.3):
    print("Order REFUSED!")
else:
    print("Order APPROVED!")
