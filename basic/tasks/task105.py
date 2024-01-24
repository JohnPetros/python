# task 105 - Write a script that contains a funcion similiar to input() function but validating the provided value to accept only numbers


def validate_number(message):
    while True:
        number = input(message)
        if not number.isnumeric():
            print("ERROR! Enter a valid number")
        else:
            break

    print(f"You entered the number {number}")


print("=" * 30)

validate_number("Enter a number: ")
