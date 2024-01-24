# task 109 - Modify the functions that were created in the task 107 so that they accept an additinal parameter,indicating whether the provided price should be formatted or not bt the function format_to_Reais developmented in the task 108

from packages.utils import money

price = float(input("Enter a price: $"))

print(
    f"The half of {price} is equal to ${money.format_to_Reais((money.get_half(price)))}"
)
print(
    f"The double of {price} is equal to ${money.format_to_Reais((money.get_double(price)))}"
)
print(
    f"Incrementing 10%, it is equal to ${money.format_to_Reais((money.increment_by_percentage(price, 10)))}"
)
print(
    f"Decrementing 20%, it is equal to ${money.format_to_Reais((money.decrement_by_percentage(price, 20)))}"
)
