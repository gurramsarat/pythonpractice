num=int(input("Enter any number : "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num," is prime number")
else:
    print(num," is not a prime number")