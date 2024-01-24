# Class 09 - Break

number = 0
total = 0

while True:
    number = int(input("Enter a number: "))

    if number == 999:
        break

    total += number

print(f"The total is {total}")
