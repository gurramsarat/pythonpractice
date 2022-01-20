salary=float(input("Enter the Salary" ))

if(salary<10000):
    da=(70/100)*salary
    hra=(65/100)*salary
    gross=salary+hra+da
    print("Gross salary..", gross)
elif(salary>=10000 and salary<=20000):
    da=(75/100)*salary
    hra=(73/100)*salary
    gross=salary+hra+da
    print("Gross salary...", gross)
else:
    da=(80/100)*salary
    hra=(76/100)*salary
    gross=salary+hra+da
    print("Gross salary....",gross)