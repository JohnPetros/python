import os


def get_file_path():
    current_directory = os.path.dirname(__file__)
    return os.path.join(current_directory, "../../../../assets/users.txt")


def get_file_content(file_path):
    with open(file_path, "rt", encoding="utf-8") as file:
        data = file.readlines()
    return data


def append_file(file_path, content):
    print(content)
    file = open(file_path, "at")
    file.write(f"\n{content}")
    file.close()


def create_file(file_path, content=""):
    file = open(file_path, "wt+")

    if len(content) > 0:
        file.write(content)

    file.close()


def check_file(file_path):
    try:
        file = open(file_path, "rt")
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True


def print_header(title):
    print("-" * 30)
    print("{:^30}".format(title))
    print("-" * 30)


def filter_users(users):
    filtered_users = list()
    for user in users:
        if user != "\n":
            filtered_users.append(user)

    return filtered_users


def show_users():
    print_header("USERS")

    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, "../../../../assets/users.txt")

    file_path = get_file_path()
    file_exists = check_file(file_path)

    if file_exists:
        users = filter_users(get_file_content(file_path))

        if len(users) > 0:
            print(f"{'ID':2}   {'Name':<20}Age")
            for user in users:
                if user != "\n":
                    id, name, age = user.replace("\n", "").split(";")
                    print(f"{int(id):2} - {name:<20}{age}")
    else:
        create_file(file_path)


def register_user():
    name = input("Name: ")
    age = int(input("Age: "))

    file_path = get_file_path()
    file_exists = check_file(file_path)

    if file_exists:
        users = filter_users(get_file_content(file_path))

        users

        last_user_id = users[-1].split(";")[0] if users else 0
        append_file(file_path, f"{int(last_user_id) + 1};{name};{age}")
    else:
        create_file(file_path, f"{1};{name};{age}")

    print_header(f"{name} registered successfully.")


def delete_user():
    while True:
        show_users()
        print()
        id = input("ID: ")

        file_path = get_file_path()

        file_exists = check_file(file_path)

        if file_exists:
            users = filter_users(get_file_content(file_path))

            new_file_content = str()
            deleted_user_name = str()

            for user in users:
                user_data = user.split(";")
                if id == user_data[0]:
                    deleted_user_name = user_data[1]
                else:
                    new_file_content += "".join(user)

            print(new_file_content)

            if deleted_user_name:
                create_file(file_path, new_file_content)
                print_header(f"{deleted_user_name} deleted successfully.")
                break
            else:
                print_header("User not found!")
                response = input("Do you wanna continue? (y/n): ").strip().lower()
                if response == "n":
                    break


def print_menu(title, options):
    print_header(title)

    for number, option in enumerate(options):
        print(f"{number + 1} - {option}")


def show_menu():
    while True:
        print_menu(
            "MAIN MENU",
            [
                "Show registered users",
                "Register new user",
                "Delete user",
                "Exit",
            ],
        )

        while True:
            try:
                option = int(input("Your option: "))

                if option not in range(1, 5):
                    raise ValueError("Please enter a valid option.")
            except ValueError as error:
                print(error)
            else:
                break

        if option == 4:
            break

        match option:
            case 1:
                show_users()
            case 2:
                register_user()
            case 3:
                delete_user()
            case _:
                print("Please enter a valid option.")

    print_header("Exiting... See you!")
