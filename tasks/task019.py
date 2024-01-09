# Task 18 - A teacher wants to randomly select one of his four students to clean the blackboard. Write a script that helps him by reading their names and displaying the chosen student's name

from random import choice

firstStudent = input('First student: ')
secondStudent = input('Second student: ')
thirdStudent = input('Third student: ')
fourthStudent = input('Fourth student: ')

chosenStudent = choice([firstStudent, secondStudent, thirdStudent, fourthStudent])

print(f'The chosen student was {chosenStudent}')
