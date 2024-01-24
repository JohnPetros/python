def validate_price(message):
    while True:
        price = input(message)

        if price != "" and not price.isalpha():
            break

        print(f"ERROR: '{price.strip()}' is not a valid price")

    return float(price.replace(",", "."))


def validate_integer(message):
    while True:
        try:
            integer = int(input(message))
        except ValueError:
            print("ERROR: enter a valid integer")
        except KeyboardInterrupt:
            print("You prefered to not provide a integer")
            return 0
        else:
            return integer


def validate_float(message):
    while True:
        try:
            float_number = float(input(message))
        except ValueError:
            print("ERROR: enter a valid floating point number")
        except KeyboardInterrupt:
            print("You prefered to not provide a floating point number")
            return 0
        else:
            return float_number
