# Task 16 - Write a script that reads any float number and displays its integer part

from math import trunc

value = float(input('Type a float value: '))

print(f'The value entered was {value} and its integer part is {trunc(value)}')

