# task 82 - Write a script in which the user enters any expression that uses parentheses. Your script should check whether or not the entered expression has the open and closed parentheses in the correct order.

expression = input("Enter a expression: ")

open_parentheses = 0
closed_parentheses = 0

for character in expression:
    if character == "(":
        open_parentheses += 1

    if character == ")":
        closed_parentheses += 1

if open_parentheses == closed_parentheses:
    print("It is a valid expression!")
else:
    print("It is not a valid expression!")
