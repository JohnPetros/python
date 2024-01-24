# Task 14 - Write a script that reads a salary of an employee and displays their new salary with a 15% increase

salary = float(input('What the salary of the employee: '))

newSalary = salary * 1.15

print(f'An employee who used to earn ${salary} will end up earning ${newSalary:.2f}')

