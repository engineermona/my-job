 
while i==1 or i==2 or i==3 or i==4 or i==5:
    for i in [1,2,3,4,5]:
        employee_list=[]
        if i==1:
            print("add new employee")
            print("enter employee data:")
            name=input("enter the name")
            age=input("enter the age")
            salary=input("enter the salary")
            employee=(f"{name} has age {age} and salary {salary}")
            employee_list.append(employee)
            i= input("enter your choise")
        if i==2:
            print("list all employees")
            if employee_list!=[]:
                 print("no employee at the moment")
                 i= input("enter your choise")
        else:
            print(employee_list)
            i= input("enter your choise")
        if i==3:
            print("delet by age ")
            age1=input("enter start age")
            age2=input("enter end age" )
            for age in range(age1,age2+1):
                pop(employee)
            i= input("enter your choise")
    if i==4:
        print ("update a salary")
        name1=input("enter your name")
        salary1=input("enter your salary")
        employee[salary]=name1
        i= input("enter your choise")
    if i==5:
         break
 raise "invalid range try again"   
 x=input("enter your choise") 
    
