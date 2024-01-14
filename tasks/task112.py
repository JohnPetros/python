# task 112 - Within the utils package created in the previous task there is a module called data. Create a function called validate_price() that should be able to work like the input() function but with a data validation to accept only monetary values.

from packages.utils import data
from packages.utils import money

price = data.validate_price("Enter a price: $")

money.get_summary(price, True)
