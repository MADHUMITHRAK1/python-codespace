b=500
PIN=1234
chances=3
print("********WELCOME TO SBI********")
while chances>=0:
    x=int(input("Enter PIN Number:"))
    if x==PIN:
        print("*****Login successful*****")
        x=int(input("Press 1 to continue:"))
    if x==1:
        print("1.Check Balance")
        print("2.Withdraw Amount")
        print("3.Exit")
        d=int(input("Enter your choice:"))
        if d==1:
            print("Your Balance is:")
            print(b)
        elif d==2:
            w=int(input("Enter the amount to be withdrawn:"))
            if w<b:
                print("Withdraw Successful")
                b=b-w
            else:
                print("Insufficient Balance")
        else:
            print('Successfully logged out')
            break
    else:
        print("*****Invalid password*****")
        chances=chances-1
        if chances==0:
            print("*****Account Blocked*****")
            break
    