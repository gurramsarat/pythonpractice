amount=int(input("Enter the withdraw money"))
a=0
b=0
c=0
if amount>=500:
    a=amount//500
    amount=amount-(a*500)
    print("500 notes are :",a)
if amount>=200:
    b=amount//200
    amount=amount-(b*200)
    print("200 notes are :",b)
if amount>=100:
    b=amount//100
    amount=amount-(c*100)
    print("100 notes are :",c)