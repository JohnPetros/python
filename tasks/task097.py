# task 97 - Write a script that contains a function that receives any text as a parameter and shows a message according to the length of the text


def super_print(message):
    lines = len(message) + 4
    print("~" * (lines))
    print(" ", message)
    print("~" * (lines))


super_print("Example of text")
super_print("Another example of text")
super_print("Text")
