def find (numbers: list)-> list:
    result=[]
    
    for i in range(len(numbers)):
            E1=[]
            for j in range(i,len(numbers)):
                number=numbers[j]
                if number in numbers:
                    print("hello")
                else:
                    E1.append(number)
                    print(number)
    return number

print(find([4,5,6,4,7,5,8]))
#[6,7,8]