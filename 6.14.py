def rndtenth():
    return (int(nmbr)*10 + 0.5)/10
def rndhundred():
    return (int(nmbr)*10 + 0.5)/100
for i in range(1,5):
    i+=1
    nmbr = input("Enter Number: ")
    print("Nearest Tenth integer for "+str(i)+" is "+str(rndtenth()))
    print("Nearest Hundred integer for " + str(i) + " is " + str(rndhundred()))

