# Task 11 - Write a script that reads the width and height of a wall in meters, calculates its area and determines the ink's amount needed to cover it, considering that each letter of ink covers an area of 2m² 

width = float(input('Wall\'s width: '))
height = float(input('Wall\'s height: '))

area = width * height

print('Your wall has the dimension of {}x{} and its area is equal to {}m²'.format(width, height, area))

print('You will need {} letters of ink to paint this wall'.format(area * 2))
