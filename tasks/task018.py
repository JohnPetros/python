# Task 18 - Write a script that reads any angle and displays the value on its sine, cosine and tangent

from math import sin, cos, tan, radians

angle = float(input('Enter a angle: '))

angleInradians = radians(angle)

sine = sin(angleInradians)
cosine = cos(angleInradians)
tangent = tan(angleInradians)

print(f'The sine is equal to {sine:.2f}')
print(f'The cosine is equal to {cosine:.2f}')
print(f'The tangent is equal to {tangent:.2f}')
