# task 113 - Write two function the first one should validate integer numbers and the second one should validate  floating point numbers. Put these functions into the data module

from packages.utils import data

integer = data.validate_integer("Enter a integer: ")
float_number = data.validate_float("Enter a floating point number: ")

if integer and float_number:
    print(f"The integer was {integer} and the floating point was {float_number}")
