# Task 7 - Write a script that reads two grades and calculate the medium between them.

firstGrade = float(input('First grade: '))
secondGrade = float(input('Second grade: '))
medium = (firstGrade + secondGrade) / 2

print('The medium between {:.1f} and {:.1f} is equal to {:.1f}'.format(firstGrade, secondGrade, medium))
