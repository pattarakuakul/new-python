
print("\t\t>>>> BMI CALCULATOR <<<<")
weight = int(input("Enter your weight in kilograms(KG): "))
height = float(input("Enter your height in Centimetre(CM): "))

#cm >> M 
height = height / 100

sum = weight / (height ** 2)
print("Your BMI is:", format(sum, '.2f'))