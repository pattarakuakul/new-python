
keep_going='Y'

while keep_going =='Y':
    wholesale = float(input("Enter the item's wholesale cost :"))

    retial_price = wholesale * 2.5

    print(f'The retial price: ${retial_price:.2f}')
    keep_going =input("Do you have another item"+ \
                  "(Enter Y for Yes): ")