# Task 66 - Write a script that reads several input integers and displays their sum. When the user enter the numbe 999 the script should stop

total = 0

while True:
    number = int(input("Enter a number [999 to stop]: "))

    if number == 999:
        break

    total += number

print(f"The total is {total}!")
