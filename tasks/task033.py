# Task 33 - Write a script that reads three numbers and displays which is the largest one and the smallest one

firstValue = int(input('first value: '))
secondValue = int(input('second value: '))
thirdValue = int(input('third value: '))

largestValue = firstValue
smallestValue = thirdValue

if secondValue > largestValue:
  largestValue = secondValue

if thirdValue > largestValue:
  largestValue = thirdValue
  
if secondValue < smallestValue:
  smallestValue = secondValue
  
if firstValue < smallestValue:
  smallestValue = firstValue
  
print(f'The largest value is {largestValue}')
print(f'The smallest value is {smallestValue}')
