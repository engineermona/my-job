number_of_sallary=int(input("enter the number"))
new_sallary=[]
for i in range(1,number_of_sallary+1):
    sallary=float(input("enter employee sallary"))
    pounce=sallary*1.20
    new_sallary.append(pounce)
print(new_sallary)    
