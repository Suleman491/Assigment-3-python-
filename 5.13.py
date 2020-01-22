nmbr=input("Enter Number to Find Factorial: ")
fact=1
for i in range(1,int(nmbr)):
    fact=fact*i
print("Facrorial of "+str(nmbr)+" is "+str(fact))
