# Task 24 - Write a script that reads the name of a city and indicates whether it starts with "santos" or not 

city = input('What is your full name? ').strip().lower()

print(city.find('santo', 0, 5) != -1)
