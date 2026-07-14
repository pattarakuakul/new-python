hours = int(input("Enter number of hours worked: "))
payrate = int(input("Enter your pay rate: "))

pay = hours * payrate
pay=float(pay)
print("The gross pay is:$ ","%.2f" % pay)
pay2 = (hours -40)*1.5*payrate + 40*payrate
pay2=float(pay)
print("The gross pay is:$ ", "%.2f" % pay)