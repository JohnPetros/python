# task 110 - Add into the module called money.py created in the previous tasks, a function called get_summary(), which displays some information generated by the functions whithin the same function.

from packages.utils import money

price = float(input("Enter a price: $"))

money.get_summary(price, True)