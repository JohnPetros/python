# Task 42 - Remake the task 35, adding the feature to displays what type of triangle will be formed:
# - EQUILATERAL: all the sides are equal
# - ISOSCELES: two sides are equal
# - SCALENE: all sides are different

side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

if (side1 + side2 < side3) or (side1 + side3 < side2) or (side2 + side3 < side1):
    print("The sides above cannot form any triangle")
else:
    if side1 == side2 and side1 == side3:
        triangle = "EQUILATERAL"
    elif (
        (side1 == side2 and side1 > side3)
        or (side3 == side2 and side3 > side1)
        or (side1 == side3 and side1 > side2)
    ):
        triangle = "ISOSCELES"
    else:
        triangle = "SCALENE"

    print(f"The sides above can form a {triangle} triangle.")
