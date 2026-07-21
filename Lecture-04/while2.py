
keep_going='Y'

while keep_going =='Y':
    sales = float(input("Enter the amount of sales:"))
    comm_rate = float(input("Enter the commission rate:"))
    
    commission = sales * comm_rate

    print(f'The commission is ${commission:.2f}')
    keep_going =input("Do you esnt to calculate another"+ \
                  "commission(Enter Y for Yes): ")