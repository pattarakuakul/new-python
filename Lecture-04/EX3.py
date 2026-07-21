import random
print("What is my magic number (1 to 100)")
mynumber = random.randint(1,100)
ntries = 1
yourguess = -1

while ntries < 7 and yourguess != mynumber:
    msg = str(ntries) +">>\t"
    if (ntries == 6):
        print("Your lsat chance EiEi")
    yourguess = int(input(msg))
    if yourguess > mynumber :
        print(" To hight Ei Ei")
    else:
        print("To low Ei Ei")
    ntries +=1
if yourguess == mynumber:
    print("Dang!! you got me >:(")
else:
    print("EZ my number is:",mynumber)

