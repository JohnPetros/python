# Task 43 - Create a logic that reads the user's weight and height, calculates their BMI and displays their status according to table bellow:
# - Underweight: bellow 18.5
# - Normal weight: between 25 and 30
# - Obesity: between 30 and 40
# - Morbid obesity: above 40

weight = float(input("What is your weight: "))
height = float(input("What is your height: "))

bmi = weight / (height**2)

print(f"Your BMI is equal to {bmi:.1f}")

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("Congratulations! You are have normal weight")
elif bmi < 30:
    print("You are over weight")
elif bmi < 40:
    print("You have obesity")
else:
    print("You are in morbid obesity, watch out!")
