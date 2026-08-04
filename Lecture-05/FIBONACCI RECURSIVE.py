def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(n)
        return fibonacci(n - 1) + fibonacci(n - 2)
        

num =int(input("Enter a number: "))

print(fibonacci(num))  # Output: 5