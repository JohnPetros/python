# Class 01 - Primitive Data Types and Output

# String
string = input('write a text: ')
print(type(string))

# Number
number = int(input('write a number: '))
print(type(number))

# Float Number
floatNumber = float(input('write a float number: '))
print(type(floatNumber))

# Boolean
number = bool(input('are you a real person?: '))
print(type(number))

# Is Numeric
value = input('write a value: ')
print(value.isnumeric())

# Is Alpha
value = input('write another value: ')
print(value.isalpha())

# Is Alpha Numeric
value = input('write another value again: ')
print(value.isalnum())