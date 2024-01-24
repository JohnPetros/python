# Task 28 - Write a script that makes the computer to think of and integer between 0 and 5 and asks the user to try to guess the chosen number. The script should indicate whether the user won or not

from random import randint 
from time import sleep

print('=' * 60)
print('What number did I think? ')
print('I will think of a number between 0 and 5. Try to guess it')
print('=' * 60)

userNumber = int(input('What number did I think of? '))

botNumber = randint(0, 5)

print('PROCESSING...')
sleep(1.5)

if userNumber == botNumber:
  print('CONGRATULATIONS! Your win!')
else:
  print(f'MY WIN! I thought the number {botNumber} and not {userNumber}')


