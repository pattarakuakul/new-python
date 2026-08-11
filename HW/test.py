charinput=("Hello Wold Hellonigger")

print("The input string is:", charinput)
emptycahr=""
for char in charinput:
    if char == " ":
        char +="-"
        print(char,"conver")
        emptycahr +=char
    else:
        print(char,"none")
        emptycahr +=char 

print(emptycahr)