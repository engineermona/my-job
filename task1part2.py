#Q8 Electricity bill
A=float(input("enter unit"))
B=A-100
C=B-100
if A<100 :
    print(nocharge)
elif 200>A>100 :
    print(5*B)
elif A>200 :
    print(5*100+C*10)
    
else :
    print()
#     #q1 percentage grade
# marks=int(input("enter marks"))
# if marks>90 :
#     print("the grade equal A") 
# elif 90>=marks>80 :
#     print("the grade equal B")
# elif 80>=marks>=60 :
#     print('the grade is C')
# elif marks<60  :
#     print("the grade is D") 
# else :
#     print() 
# #Q2 cost price of a bike

# cost=int(input("enter the cost-price"))
# if cost>100000:
#     print (tax=0.15*cost)

# elif 100000>cost>50000 :
#     print(tax=0.1*cost)

# elif cost<=50000 :
#     print(0.05*cost)
# else :
#     print() 
# # Q5 LARGEST NUMBER OUT OF TWO NUMBERS EXCEPTED FROM USER 


# #Q6 CHECK THE NUMBER IS POSITIVE OR NEGATIVE
# number=int(input("enter the number"))
# print("positive") if number>=0 else print("negative") 
# number_2=int(input("enter the number")) 
# # q7 even or odd
# print("even") if number_2 % 2 == 0 else print("odd")
# #Q1 PERCENTAGE OF ATTENDENCE
# working_day=int(input("enter total number of working days"))
# absent_day=int(input("total number of days for absent"))
# attendence=working_day-absent_day
# percent_attendence=attendence/working_day*100
# if percent_attendence<75 :
#     print("the student will not be able to sit in exam")
# else :
#     print()    
# #q2 percentage and grade 
# student_grade=int(input("enter your percentage"))
# if student_grade<25 :
#     print("D")
# elif 45>student_>grade>25 :
#     print ("C")
# elif 50>student_>grade>45 :
#     print("B")
#  elif 60>student_grade>50 :
#     print ("B+")
# elif student_grade>80 :
#     print ("A+")  
#  else :
#     print ()    