# Task 4 - Write a script that reads something and displays its primtive type and all information about it.

value = input('Write something: ')

print(f'The primitive data type of this value is {type(value)}')
print(f'Is it only blank space? {value.isspace()}')
print(f'Is it a number? {value.isnumeric()}')
print(f'Is it a alpha? {value.isalpha()}')
print(f'Is it a alpha numeric? {value.isalnum()}')
print(f'Is it in uppercase? {value.isupper()}')
print(f'Is it in lowercase? {value.islower()}')
print(f'Is it in captalised? {value.istitle()}')