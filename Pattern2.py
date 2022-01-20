count=9
count2=91
for i in range(5):
    for j in range(5):
        if i%2==0:
            count=count+1
            print(count,end=" ")
        else:
            count2=count2-1
            print(count2,end=" ")
    print()
        