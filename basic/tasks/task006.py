# Task 6 - Write a script that reads a integer and displays its double, triple and square root.

number = int(input('Write a number: '))

print(f'Double of {number} is {number * 2}')
print(f'Triple of {number} is {number * 3}')
print('Square root of {} is {:.2f}'.format(number, number ** 0.5))
