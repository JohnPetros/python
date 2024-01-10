# Task 40 - Write a script that reads two grades of a student and calculates the medium, displaying a message in the end, based on the reached medium:
# - Medium bellow 4.9: REPROVED
# - Medium between 5.0 and 6.9: IN RECOVERY
# - Medium above or equal to 7: APPROVED

grade1 = float(input("First grade: "))
grade2 = float(input("Second grade: "))

medium = (grade1 + grade2) / 2

print(f"Taking {grade1:.1f} and {grade2:.1f}, the medium will be {medium:.1f}")

if medium <= 4.9:
    print("The student is REPROVED")
elif medium <= 6.9:
    print("The student is IN RECOVERY")
else:
    print("The student is APPROVED")
