# task 96 - Write a script that contains a function that receives the dimensions of a land (width and length) and shows its area


def calculate_area(width, length):
    area = width * length
    print(f"A land of {width}x{length} is {area}m²")


print("-" * 15)
print("{:^15}".format("Control of Land"))
print("-" * 15)

width = float(input("Width (m): "))
length = float(input("Length (m): "))

calculate_area(width, length)
