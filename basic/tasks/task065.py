# Task 65 - Write a script that reads several input integers. At the end, display the average of all the integers and what was the largest and smallest integers read. The script should ask the user whether or not they want to continue entering the integers

canContinue = True
total = 0
numbers = 0
largest = 0
smallest = 0
response = ""

while canContinue:
    number = int(input("Enter a number: "))
    response = ""

    while response not in ["Y", "N"]:
        response = input("Do you want to continue? [Y/N]: ").strip().upper()
        if response not in ["Y", "N"]:
            print("Ivalid response.")

    numbers += 1
    total += number

    if numbers == 1:
        smallest = number

    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

    canContinue = response == "Y"


print(f"You entered {numbers} numbers and the medium was {(total / numbers):.2f}.")
print(f"The largest number was {largest} and the smallest was {smallest}.")
