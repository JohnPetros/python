# task 69 - Write a script that reads the age and gender of several people. At each registered person, the script should ask whether or not the user want to continue. At the end display:
# The amount of people over 18
# The amount of registered men
# The amount of women under 20

response = "Y"

peopleOfLegalAge = 0
men = 0
womenUnder20 = 0

while response == "Y":
    print("-" * 30)
    print("{:^30}".format("REGISTER A PERSON"))
    print("-" * 30)

    age = int(input("Age: "))
    gender = input("Gender [M/F]: ").strip().upper()

    if age >= 18:
        peopleOfLegalAge += 1

    if gender == "M":
        men += 1

    if gender == "F" and age < 20:
        womenUnder20 += 1

    while True:
        response = input("Do you want to continue? [Y/N]: ").strip().upper()

        if response not in ["Y", "N"]:
            print("Ivalid response! Please, enter Y (yes) or N (no).")
        else:
            break


print(f"The total of people over 18: {peopleOfLegalAge}")
print(f"In total there are {men} men registered")
print(f"In total there are {womenUnder20} women under 20 registered")
