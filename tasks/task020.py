# Task 18 - The same teacher from the previous task wants to randomly select the presentation order of the students' projects. Write a script that reads the names of the four students and displays the randomly chosen order.

from random import shuffle

firstStudent = input('First student: ')
secondStudent = input('Second student: ')
thirdStudent = input('Third student: ')
fourthStudent = input('Fourth student: ')

students = [firstStudent, secondStudent, thirdStudent, fourthStudent]
shuffle(students)

print(f'The order of the presentation will be {students}')
