def validate_price(message):
    while True:
        price = input(message)

        if price != "" and not price.isalpha():
            break

        print(f"ERROR: '{price.strip()}' is not a valid price")

    return float(price.replace(",", "."))
