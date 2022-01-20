n=int(input("Enter a number: "))
sum=0
for y  in range(2,n,1):
    if y>1:
        for i in range(2,y,1):
            if (y%i)==0:
                break
            else:
                sum=sum+1
                if(sum%2==0):
                    continue
                else:
                    print(y)