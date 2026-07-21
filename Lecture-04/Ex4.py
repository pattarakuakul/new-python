columns =int(input("Enter your columns >>"))
number=0
for i in range(0,100,1):
    if number == 100:
            break
    for j in range(columns):
        if number == 100:
            break
        number = number +1
        print(number,"\t",end="")
    print()