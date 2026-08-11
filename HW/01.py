def format_strings(*args):
    result_of_string = ""

    for char in args:
         if char == " ":
            result_of_string += "-"
         else:
            print(char)
            upper_str = char.upper()
            result_of_string += upper_str

    return result_of_string

if __name__ == '__main__':
    result = format_strings("Hello", "world", "this", "is", "a", "test")
    print(result)  # Output: "HELLOWORLDTHISISATEST"

    result = format_strings("Python", "is", "fun")
    print(result)  # Output: "PYTHONISFUN"

    result = format_strings("Hello world")
    print(result)  # Output: "HELLO-WORLD"
