nums =list(map(int,("Enter number list :").split()))
target=int(input("Enter the target number :"))
print (nums)
output = []
for numberloop1 in nums: 
        for numberloop2 in nums:
                sum= numberloop1 * numberloop2
                if sum == target:
                    if [numberloop2,numberloop1] not in output and numberloop1 != numberloop2:
                        output.append([numberloop1,numberloop2])
    
print ("OUTPUT HERE >>",output)
