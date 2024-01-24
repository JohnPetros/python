# Task 1 - A special event is set to start in 10 seconds. Count down from 0 to 10 with a one second pause between each number

import time

for second in range(10, -1, -1):
    print(second, end=" ", flush=True)
    time.sleep(1)
