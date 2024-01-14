# task 108 - Create a module named "money" that includes the built-in functions get_half(), get_double(), increment_by_percentage() and decrement_by_percentage(). Also write a script the imports this module and use some of these functions.

from packages.utils import money

price = float(input("Enter a price: $"))

print(f"The half of {price} is equal to ${(money.get_half(price))}")
print(f"The double of {price} is equal to ${(money.get_double(price))}")
print(f"Incrementing 10%, it is equal to ${(money.increment_by_percentage(price, 10))}")
print(f"Decrementing 20%, it is equal to ${(money.decrement_by_percentage(price, 20))}")
