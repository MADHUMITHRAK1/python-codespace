print("Select the type of connection:")
print("1.Residential")
print("2.Commercial")
print("3.Industrial")
connection_type=int(input("Enter your choice(1/2/3):"))
units=int(input("Enter the number of units consumed:"))
if connection_type==1:
    if units<=100:
        bill=units*5
    elif units<=300:
        bill=(100*5)+(units-100)*7
    else:
        bill=(100*5)+(200*7)+(units-300)*10
elif connection_type==2:
    if units<=100:
        bill=units*8
    elif units<=300:
        bill=(100*8)+(units-100)*10
    else:
        bill=(100*8)+(200*10)+(units-300)*12
elif connection_type==3:
    if units<=100:
        bill=units*10
    elif units<=300:
        bill=(100*10)+(units-100)*15
    else:
        bill=(100*10)+(200*15)+(units-300)*20
else:
    print("Invalid choice:Please restart the program.")
    bill=None
if bill is not None:
    print("The electricity bill for",units,"units is: Rs.",bill)

