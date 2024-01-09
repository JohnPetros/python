# Task 29 - Write a script that reads the speed of a car. If it exceeds 80Km/h, display a message informing that the driver has been fined. The fine will cost $7.00 for each km above the speed limit

speed = int(input('What is the current speed of the car? '))

limit = 80

if speed > limit:
  print(f'You have been fined! You exceeded the permitted speed limit, which is {limit}Km/h')
  print(f'You must pay a fine of ${((speed - limit) * 7):.2f}')

print('Have a good day! Drive safely!')


