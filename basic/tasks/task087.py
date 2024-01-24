# task 87 - Enhance the previous script, displaying at the end:
# - The total of all items in the matrix
# - The total of all items from the matrix's third column
# - The largest number from the matrix's second line

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for line in range(0, len(matrix)):
    for column in range(0, len(matrix[line])):
        matrix[line][column] = int(input(f"Enter value of [{line}, {column}]: "))


print("-=" * 20)

for list in matrix:
    for item in list:
        print(f"[{item:^5}]", end="")
    print(end="\n")

print("-=" * 20)

total = 0
third_list_total = 0
second_list_largest_number = 0

for list_position, list in enumerate(matrix):
    for item_position, item in enumerate(list):
        total += item
        if item_position == 2:
            third_list_total += item

    if list_position == 1:
        for item_position, item in enumerate(list):
            if item_position == 0:
                second_list_largest_number = item
            else:
                if item > second_list_largest_number:
                    second_list_largest_number = item

print(f"The total is {total}")
print(f"The total of even items from the third column is {third_list_total}")
print(f"The largest item from the second line is {second_list_largest_number}")
