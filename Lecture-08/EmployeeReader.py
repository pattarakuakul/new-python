i=0
with open("employee.txt","r") as emp_file:
    
    for lines in emp_file:
        line = lines.strip()
        print("____________")
        print(i)
        print("____________")
        i += 1
        if i ==1 and i !="":
            print("Employee Name:",line)
        elif i ==2 and i !="":
            print("Employee ID:",line)    
        elif i ==3 and i !="":
            print("Employee Department:",line)
        elif i == 4 and i !="":
            print()
            i = 0
    

    xxxxxxxxxxxx