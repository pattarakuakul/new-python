def is_armstrong(number):
    number = str(number)
    number_of_digits = len(number)
    Initialize = 0
    for digit in str(number):
        Initialize += int(digit) ** number_of_digits
    return Initialize == int(number)

print(is_armstrong(123))  # True