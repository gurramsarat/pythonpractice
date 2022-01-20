units=int(input("Enter the units"))
if( units<=50):
    bills=0.75*units
elif(units<=150):
    bills=(50*0.75)+(units-50)*2.10
elif(units<=250):
    bills=(50*0.75)+(100*2.10)+(units-150)*2.50
else:
    bills=(50*0.75)+(100*2.10)+(100*25.0)+(units-250)*2.80


print("Bills: ",bills)
gst=(bills*10)/100
bills=bills+gst
print("Gst:",gst)
print("final bill: ",bills)
    