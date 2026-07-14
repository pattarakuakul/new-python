hours = int(input("Enter number of hours worked: "))
payrate = int(input("Enter your pay rate: "))

if hours <= 40:
    pay = hours * payrate
    pay=float(pay)
    print("The gross pay is:$ ","%.2f" % pay)
if hours > 40:
    pay = (hours -40)*1.5*payrate + 40*payrate
    pay=float(pay)
    print("The gross pay is:$ ", "%.2f" % pay)