count = 1
cnt=1
a=input("Enter Ten Numbers: ")
fmax=0
smax=0
while(count<10):
    a = input("Enter Ten Numbers: ")
    count += 1
    if(fmax<int(a)):
        smax=fmax
        fmax=int(a)
    elif(smax<int(a)):
        smax=int(a)


print("First Maximum Number is: "+str(fmax))
print("Second Maximum Number is: "+str(smax))
