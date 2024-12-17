s1=int(input("Enter the first side of the triangle:"))
s2=int(input("Enter the second side of the triangle:"))
s3=int(input("Enter the third side of the triangle:"))
if (s1==s2) and (s1==s3):
    print("Equilateral Triangle.")
elif (s1==s2) or (s1==s3):
    print("Isosceles Triangle.")
elif (s1!=s2) and (s1!=s3):
    print("Scalane Triangle.")
else:
    print("Invalid Input")