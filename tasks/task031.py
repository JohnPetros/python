# Task 31 - Write a script that asks the distance of a trip in Km. Calculate the trip's price, charging $0.50 per Km for trips up to 200Km and $0.45 for longer trips 

distance = float(input('What is the distance of your trip in Km? '))

price = distance * .5 if distance <= 200 else distance * .45

print(f'You are about to start a trip of 150Km\nAnd your ticket price will be ${price:.2f}')




