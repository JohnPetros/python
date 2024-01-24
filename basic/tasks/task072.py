# task 72 - Write a script that has a tuple completely filled with numbers in the range from zero to twenty. Your script should read a number and display its name.

numberNames = (
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
)


while True:
    number = int(input("Enter a number between 0 and 20: "))

    if number not in range(0, 21):
        print("Try again. ", end="")
    else:
        print(f"You entered the number {numberNames[number]}.")
        break
