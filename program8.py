print("For calculating the simple interest,enter the following details:")
p_amt=int(input("Enter the principal amount:"))
rate_of_int=float(input("Enter the rate of interest:"))
time=int(input("Enter the time period:"))
interest=(p_amt*rate_of_int*time)/100
print("The rate of simple interest is:",interest)