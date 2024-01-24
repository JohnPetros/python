def format_to_Reais(price):
    return f"R${price:.2f}".replace(".", ",")


def get_half(price, should_format=False):
    result = price / 2

    return format_to_Reais(result) if should_format else result


def get_double(price, should_format=False):
    result = price * 2

    return format_to_Reais(result) if should_format else result


def increment_by_percentage(price, percentage, should_format=False):
    result = price * (1 + (percentage / 100))

    return format_to_Reais(result) if should_format else result


def decrement_by_percentage(price, percentage, should_format=False):
    result = price * (1 - (percentage / 100))

    return format_to_Reais(result) if should_format else result


def get_summary(prince, should_format=False):
    print("-" * 35)
    print("{:^35}".format("SUMMARY OF THE PRICE"))
    print("-" * 35)

    print(f"Analysed price: \t{(format_to_Reais(prince) if should_format else prince)}")
    print(f"Double of the price: \t{get_double(prince, should_format)}")
    print(f"Half of the price: \t{get_half(prince, should_format)}")
    print(f"80% increase: \t\t{increment_by_percentage(prince, 80, should_format)}")
    print(f"35% decrease: \t\t{decrement_by_percentage(prince, 35, should_format)}")
