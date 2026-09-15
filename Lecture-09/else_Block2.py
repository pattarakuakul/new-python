def divide (a,b):
    try :
        result = a/b
    except ZeroDivisionError as e:
        print("Exception :",e)
        return None
    else:
        return result
    
a,b = map(int, input("Enter number:  ") .split())
print(divide(a,b))
print("End of program")

