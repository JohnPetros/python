# task 86 - Write a script that creates a 3x3 matrix and fills it with the entered values. Finally, display the matrix in the correct format

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for line in range(0, len(matrix)):
    for column in range(0, len(matrix[line])):
        matrix[line][column] = int(input(f"Enter value of [{line}, {column}]: "))


print("-=" * 20)

for list in matrix:
    for item in list:
        print(f"[{item:^5}]", end="")
    print(end="\n")
