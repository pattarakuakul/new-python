print("Please select operation -\n1. add\n2. subtract\n3. multiply\n4. divide")
operation = int(input("Select operation from 1, 2, 3, 4 :"))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operation == 1:
    sum = num1 + num2
    print(num1, "+", num2, "=", sum)
if operation == 2:
    sum = num1 - num2
    print(num1, "-", num2, "=", sum)
if operation == 3:
    sum = num1 * num2
    print(num1, "*", num2, "=", sum)
if operation == 4:
    sum = num1 / num2
    print(num1, "%", num2, "=", sum)