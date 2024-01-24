# task 67 - Write a script that displays the multiplication table for several numbers, one at a time, for each value etered by the user. The script will stop when the entered number is negative.

while True:
    print("-" * 80)
    number = int(input("What number do you want to see the multiplication table of? "))
    print("-" * 80)

    if number == -9:
        break

    for multiplicator in range(1, 11):
        print(f"{number} x {multiplicator:2} = {number * multiplicator}")


print("The script is finished! Thank of your business.")
