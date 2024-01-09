# Task 23 - Write a script that reads a number from 0 to 9999 and displays each of its digits separately

number = str(int(input('Enter a number: '))).zfill(4)

thousands = number[-4]
hundreds = number[-3]
tens = number[-2]
units = number[-1]

print(f'Thousands: {thousands}')
print(f'Hundreds: {hundreds}')
print(f'Tens: {tens}')
print(f'Units: {units}')

# Other solution

thousands = number // 1 % 10
hundreds = number // 10 % 10
tens = number // 100 % 10
units = number // 1000 % 10

print(f'Thousands: {thousands}')
print(f'Hundreds: {hundreds}')
print(f'Tens: {tens}')
print(f'Units: {units}')