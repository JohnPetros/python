# Task 28 - Write a script that 

from random import randint 
from time import sleep

print('=' * 60)
print('What number did I think? ')
print('I will think a number between 0 and 5. Try to guess it')
print('=' * 60)

userNumber = int(input('What number did I think? '))

botNumber = randint(0, 5)

print('PROCESSING...')
sleep(1.5)

if userNumber == botNumber:
  print('CONGRATULATIONS! Your win!')
else:
  print(f'MY WIN! I thought the number {botNumber} and not {userNumber}')


