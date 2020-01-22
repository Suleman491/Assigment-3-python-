nmbr = input("Number of Values: ")
smallest=int(nmbr)
while(int(nmbr)>0):
    value = input("Value: ")
    if(int(value)<smallest):
        smallest=int(value)
    nmbr=int(nmbr)-1
print("Smallest Value is: "+str(smallest))

