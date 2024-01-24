# task 90 - Write a script that reads the name and avearage of student and puts them into a dictionary. At the end, display these attributes.

student = dict()

student["name"] = input("Name: ")
student["average grade"] = int(input("Average Grade: "))

print("-=" * 30)

print(f"Student's is {student['name']}")
print(f"Studen's average is {student['average']}")
