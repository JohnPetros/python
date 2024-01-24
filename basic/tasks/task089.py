# task 89 - Write a script that reads the name and two grades of a several students and places all of them into a list. At the end, display a report card containing the average grade of each one of them and allows the user to show the grades of each student individually

students = []

while True:
    student = []

    name = input("Name: ").strip()
    grade1 = float(input("Grade 1: "))
    grade2 = float(input("Grade 2: "))

    student = [name, [grade1, grade2]]

    students.append(student)

    while True:
        response = input("Do you want to continue? [Y/N]: ").strip().upper()
        if response not in ["Y", "N"]:
            print("Ivalid response! Please, enter Y (yes) or N (no).")
        else:
            break

    if response == "N":
        break

print(f'{"Num.":<5}{"Name":<10}{"Average":>10}')
print("-" * 25)
for position, student in enumerate(students):
    print(f"{position:<5}", end="")
    print(f"{student[0]:<10}", end="")
    print(f"{((student[1][0] + student[1][1]) / 2):>10.1f}")
print("-" * 25)

while True:
    while True:
        number = int(input("Which student to show their grades? [999 to stop]: "))
        if number > len(students) - 1 and number != 999:
            print("Student not found! Try again.")
        else:
            break

    if number == 999:
        break

    student = students[number]

    print("-" * 25)
    print(f"{student[0]}'s grades are: {student[1]}")
    print("-" * 25)


print("EXITING...")
print("<<< Thank your business >>>")
