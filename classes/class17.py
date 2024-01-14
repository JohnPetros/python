# Class 17 - Errorr and Exceptions

try:
    a = float(input("Numerator: "))
    b = float(input("Denominator: "))
    r = a / b
except (ValueError, TypeError):
    print("We had a problem with the types of the values you entered!")
except ZeroDivisionError:
    print("It is not possible to divide a value by zero!")
except KeyboardInterrupt:
    print("The user chose to not input data!")
except Exception as error:
    print(f"The caught exception was {error.__cause__}.")
else:
    print(f"The result is {r}")
finally:
    print("Thank your business")
