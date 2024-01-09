# Task 12 - Write a script that reads the price of a product and displays its new price at 5% off

price = float(input('What is the price of the product: '))

print('The product which was priced at ${:.2f}, will cost ${:.2f} with 5% discount during the promotion'.format(price, price * 0.95))

