a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
op=input("Enter the calculation to be done(+,-,*,/):")
if op=='+':
    print("Result:",a+b)
elif op=='-':
    print("Result:",a-b)
elif op=='*':
    print("Result:",a*b)
elif op=='/':
    print("Result:",a/b)
else:
    print("Invalid Output!")