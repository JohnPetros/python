# Task 59 - Writes a script that reads two values and displays a menu with the following table:
# [ 1 ] sum
# [ 2 ] multiply
# [ 3 ] largest
# [ 4 ] new numbers
# [ 5 ] exit
# Your script must do the ordered operation for each case

from time import sleep

firstValue = int(input("First value: "))
secondValue = int(input("Second value: "))

option = 0

while option != 5:
    print(
        """[ 1 ] sum   
[ 2 ] multiply
[ 3 ] largest   
[ 4 ] new numbers 
[ 5 ] exit"""
    )

    option = int(input(">>>>> What is your option? "))

    match option:
        case 1:
            print(
                f"The sum of {firstValue} and {secondValue} is equal to {firstValue + secondValue}"
            )
        case 2:
            print(
                f"The multiplication of {firstValue} and {secondValue} is equal to {firstValue * secondValue}"
            )
        case 3:
            print(
                f"The largest number is {firstValue if firstValue > secondValue else secondValue}"
            )
        case 4:
            firstValue = int(input("First value: "))
            secondValue = int(input("Second value: "))
        case 5:
            print("Exiting...")
            sleep(1)
        case _:
            print("Invalid option. Try again!")

    print("=" * 15)

print("End of the script! Thank you for your business.")
