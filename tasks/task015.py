# Task 14 - Write a script that asks the amount of Km by a rented car and the amount of days for which it was rentaled. Calculate the price to pay, considering the car costs $60.00 per day and $0.15 per km driven

days = float(input('How much days the car was rented for: '))
kms = float(input('How much Km was driven by the car: '))

total = days * 60 + (kms * 0.15)

print(f'The total to pay is equal to ${total :.2f}, ')

