# Task 32 - Write a task that reads a year and displays whether it is a leap year or not

from datetime import date

year = int(input('What year do you want to analyse? Enter 0 for analyse the current one: '))

if year == 0:
  year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  print(f'The year {year} IS A LEAP YEAR')
else:
  print(f'The year {year} IS NOT A LEAP YEAR')
  





