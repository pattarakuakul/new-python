try:
    value = int(input("Enter a number :"))
    result = 10 / value
except ValueError:
    print("Invalid Input! Please enter number.")
except ZeroDivisionError:
    print("Cannot divide by zero")
print()
print(result)
print("____________________________")
print("End of program")
