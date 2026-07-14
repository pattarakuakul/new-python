employeesnum_employees = int(input("Enter the number of employees: "))

if employeesnum_employees < 50:
    print("This is small company")
elif employeesnum_employees < 250:
    print("This is medium-sized company")
elif employeesnum_employees >= 250:
    print("This is a large company")
else:
    print("Error")

