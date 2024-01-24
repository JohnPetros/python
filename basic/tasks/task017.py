# Task 17 - Write a script that reads the widths of the opposite and adjacent sides of a right-angled triangle, calculates, and displays the width of the hypotenuse.

from math import pow, sqrt

oppositeSide = float(input('The width of the opposite side: '))
adjacentSide = float(input('The width of the adjacent side: '))

hypotenuse = sqrt(pow(oppositeSide, 2) + pow(adjacentSide, 2))

print(f'The hypotenuse is equal to {hypotenuse:.2f}')

