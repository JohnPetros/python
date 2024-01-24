# Task 37 - Write a script that reads any integer and asks the user to choose which base will be used for the conversion

number = int(input("Enter a number: "))

print("Choose a base for the conversion:")
print("[ 1 ] convert to BINARY")
print("[ 2 ] convert to OCTAL")
print("[ 3 ] convert to HEXADECIMAL")

option = int(input("The house's price: "))

if option == 1:
    print(f"{number} to BINARY is equal to {bin(number)[2:]} ")
elif option == 2:
    print(f"{number} to OCTAL is equal to {oct(number)[2:]} ")
elif option == 3:
    print(f"{number} to HEXADECIMAL is equal to {hex(number)[2:]} ")
else:
    print("Invalid option! Try again!")
