# Task 34 - Write a script that asks for an employee's salary and calculates the amount of their raise. For salaries above $1.200.00, calculate a raise of 10%. For salaries equal to or below, the raise is 15%.

salary = float(input('What is the employee\'s salary: '))

salaryRaise = 1.15 if salary <= 1200 else 1.1

print(f'Who used to earn ${salary} will end up earning ${(salary * salaryRaise):.2f} now')
