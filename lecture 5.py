students=int(input("enter number of students"))
new_student=[]
for i in range(1,students+1) :
    student=input("enter the name").strip().capitalize()
    new_student.append(student)
print(new_student)
