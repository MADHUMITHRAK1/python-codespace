student={'name':'','class':'','marks':{'math':0,'science':0,'english':0}}
student['name']=input("Enter the student's name:")
student['class']=input("Enter the student's class:")
student['marks']['math']=float(input("Enter the student's math mark:"))
student['marks']['science']=float(input("Enter the student's science mark:"))
student['marks']['english']=float(input("Enter the student's english mark:"))
total_marks=sum(student['marks'].values())
percentage=total_marks/300*100
percentage=round(percentage,2)
print("\n\n**********STUDENT MARKSHEET***********")
print("Name of the student:",student['name'])
print("Class of the student:",student['class'])
print("Math mark:",student['marks']['math'])
print("Science mark:",student['marks']['science'])
print("English mark:",student['marks']['english'])
print("Total marks:",total_marks)
print("Percentage:",percentage)
print("**************************************")