# Task 57 - Writes a script that reads the user's gender, but only accepts the values "F" (female) or "M" (male). In the case of an invalid response, asks for the input again until a valid response is obtained

response = input("Inform your gender (M/F): ").strip().upper()

while response not in ["F", "M"]:
    print('Invalid response. Please, only the values "F" and "M" are allowed. ', end="")
    response = input("Inform your gender (M/F): ").strip().upper()

print("Male" if response == "M" else "Female", "gender successfully recorded.")
