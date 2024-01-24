# task 107 - Make a mini system that uses the interactice help from Python. The user will enter command and its manual should be shown. When the user enters "exit" the script should be finished


def show_header(title):
    print("~" * 30)
    print("{:^30}".format(title))
    print("~" * 30)


def custom_help(resource):
    show_header(f"SHOWING THE MANUAL OF '{resource}'")
    help(resource)


show_header("HELP SYSTEM PYTHELP")

while True:
    resource = input("Function or library > ")

    if resource == "exit":
        break

    custom_help(resource)

print("SEE YA!")
