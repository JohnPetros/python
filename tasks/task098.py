# task 98 - Write a script that contains a function that receives three parameters: first_number, last_number, step. Your script should perform 3 counts through this function
# A) From 1 to 10, step by 1
# B) From 10 to 0, step by 2
# C) A personlized counting

from time import sleep


def count_numbers(first_number, last_number, step):
    stop = last_number - 1 if first_number > last_number else last_number + 1

    if first_number > last_number:
        _step = -abs(step)
    elif first_number < last_number and step < 0:
        _step = abs(step)
    else:
        _step = step

    print("-=" * 30)
    print(f"Count starting from {first_number} to {last_number} step by {abs(step)}")

    for counter in range(first_number, stop, _step):
        print(f"{counter}", end=" ", flush=True)
        sleep(0.5)

    print("END!")
    print("-=" * 30)


count_numbers(1, 10, 1)
count_numbers(10, 0, 2)

print("Now it is your turn to personalize the count!")

first_number = int(input("first number: "))
last_number = int(input("last number: "))
step = int(input("Step: "))


count_numbers(first_number, last_number, step)
