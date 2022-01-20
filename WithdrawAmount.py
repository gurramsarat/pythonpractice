amount=int(input("Enter the withdraw money"))
a=0
b=0
c=0
d=0
e=0
if amount%10==0 and amount>0:
   if amount>=200:
      a=amount//200
      amount=amount-(a*200)
      print("200 notes are :",a)
   if amount>=100:
      b=amount//100
      amount=amount-(b*100)
      print("100 notes are :",b)
   if amount>=50:
      c=amount//50
      amount=amount-(c*50)
      print("50 notes are :",c)
   if amount>=20:
      d=amount//20
      amount=amount-(d*20)
      print("20 notes are :",d)
   if amount>=10:
      e=amount//10
      amount=amount-(e*10)
      print("10 notes are :",e)
else:
      print("Invalid Amount")
 
    