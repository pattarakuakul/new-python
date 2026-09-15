try :
    numerator = float(input("Enter the numerator:"))
    denominator = float(input("Enter the denominator:"))

    result = numerator / denominator
    print(f"The result is {result}")
except ZeroDivisionError:
    print("Error: Invalid input. Please enter numeric values.")
except ValueError as e:
    print(f"Enter Number!! not {e}")
finally:
    print("End of program")