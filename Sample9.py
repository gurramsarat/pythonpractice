x=int(input("Enter the Number "))
y=int(input("Enter the Number "))
z=int(input("Enter the Number "))
if(x>y and x>z):
    print("Maximum number x",x)
elif(y>x and y>z):
    print("Maximum number y",y)
else:
    print("Maximum number z",z)