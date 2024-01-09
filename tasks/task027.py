# Task 27 - Write a script that reads the user' full name and displays their first name and last name

fullName = input('Enter your full name: ').strip()

splittedName = fullName.split(' ')

firstName = splittedName[0]

lastName = splittedName[-1]

print('Really nice to meet you!')
print(f'Your first name is {firstName}')
print(f'Your last name is {lastName}')
