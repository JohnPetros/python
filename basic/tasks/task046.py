# Task 46 - Write a script that displays a countdown to the fireworks explosion ranging from 10 to 0 with a pause of 1 second between each number

import time

for counter in range(10, -1, -1):
    print(counter)
    time.sleep(1)

print("BOM BOM BUM!")
