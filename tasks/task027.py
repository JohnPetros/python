# Task 24 - Write a script that reads a phrase and displays
# - How many times does the letter "A" appear in the phrase
# - At what position does the letter "A" first appear in the phrase
# - At what position does the letter "A" last appear in the phrase

fullName = input('Enter your full name: ').strip()

splittedName = fullName.split(' ')

firstName = splittedName[0]

lastName = splittedName[-1]

print('Really nice to meet you!')
print(f'Your first name is {firstName}')
print(f'Your last name is {lastName}')
