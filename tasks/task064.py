# Task 64 - Write a script that reads several integers. The script will only stop when the use enter the number 999 which is the stopping condition. At the end, display the amount of integers entered and their sum (ignoring the flag)

canStop = False

total = 0
numbers = 0

while not canStop:
    number = int(input("Enter a number [999 to stop]: "))

    if number == 999:
        canStop = True
    else:
        total += number
        numbers += 1

print(f"You entered {numbers} numbers and the sum of them is {total}.")
