print("your Score Max(100)")
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

sum = (number1+number2+number3)/3

print("The average of the three numbers is: ", sum)
if sum > 95:
    print("Congratulations!")
    print("That is a great average!")
else:
    print("your score is too low Try again!!")