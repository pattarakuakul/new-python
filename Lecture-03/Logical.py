x =int(input("Enter first number: "))
y =int(input("Enter second number: "))
z =int(input("Enter third number: "))
# use and
if x > y and x > z:
    print("x is less than y and y is less than z.\n")
# use or
if x < y or y > z:
    print("Either x is less than y or y is greater than z.\n")
# use not
if not (x > y):
    print("x is not greater than y.\n")