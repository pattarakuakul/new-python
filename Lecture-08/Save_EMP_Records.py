num_emp = int(input("How many employee do you want to create? "))
with open ("employee.txt","w") as emp_file:
    for count in range(1,num_emp + 1):
        print("Enter data for employee #",count,sep="")
        name = input("Name: ")
        id_num = input("ID  number: ")
        dept = input("Department: ")
        emp_file.write(name + "\n")
        emp_file.write(id_num + "\n")
        emp_file.write(dept + "\n")
        print()

print("Employee records written to employee.txt.")
