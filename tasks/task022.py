# Task 22 - Write a script that reads a person's full name and displays:
# - The name in all uppercase and lowercase letters. 
# - How many letters in total (not considering spaces) 
# - How many letters are there in the first name (excluding spaces) 

fullName = input('Type your full name: ').strip()

splitedName = fullName.split(' ')

nameWithoutSpaces = ''.join(splitedName)

fullname = ' '.join(list(filter(None, splitedName)))

firstName = splitedName[0]

print(f'Your name in uppercase is {fullname.upper()}')
print(f'Your name in lowercase is {fullname.lower()}')
print(f'There are about {len(nameWithoutSpaces)} letters in your name')
print(f'Your first name is {firstName} and there are {len(firstName)} letters in it')
