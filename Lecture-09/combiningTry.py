try:
    value = int(input("Enter a number: "))
    result = 10/value
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("cannot divide by zero!!!!")
else:
    print(f"The result is {result}")
finally:
    print("Execution Completed.")

print("END")