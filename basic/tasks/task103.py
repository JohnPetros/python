# task 103 - Write a script that contains a funcion that will receive two parameters: the first will indicate the number from which the factorial will be calculated, the second, which is a boolean (optional), will indicate whether the factorial calculatation should be shown or not.


def calculate_factorial(number, should_show: bool = False):
    factorial = 1

    while number >= 1:
        factorial *= number

        if should_show:
            print(f"{number}", end="")
            if number != 1:
                print(" x ", end="")
            else:
                print(" = ", end="")

        number -= 1

    print(f"{factorial}")


calculate_factorial(5, should_show=True)
