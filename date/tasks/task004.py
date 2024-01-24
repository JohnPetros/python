# Task 4 - Suppose that you are working for a company that wants to monitor the customer's activity. One metric that they interested in is the passed time since the last transaction of the customer. Write a script that displays how long it has been since the last customer's purchased (May 10, 2023). If it is more than 30 days, display a message offering a discount to the customer

from datetime import datetime

last_date = datetime(2023, 5, 10)

current_date = datetime.now()

difference_days = current_date - last_date

if difference_days.days > 30:
    print("You can have a discount")
else:
    print("You cannotj have a discount")
