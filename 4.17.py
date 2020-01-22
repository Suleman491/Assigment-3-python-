count=1
a=input("Enter Ten Numbers: ")
fmax=0
smax=0
tmax=0
while(count<10):
    a = input("Enter Ten Numbers: ")
    count+=1
    if(fmax<int(a)):
        tmax=smax
        smax=fmax
        fmax=int(a)
    elif(tmax<int(a)):
        tmax=smax
        smax=int(a)
    elif(smax<int(a)):
        tmax=int(a)
    count


print("First Maximum Number is: "+str(fmax))
print("Second Maximum Number is: "+str(smax))
print("Third Maximum Number is: "+str(tmax))
